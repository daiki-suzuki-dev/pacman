import requests
import os
import csv
import json
import time

# -----------------------------
# CONFIGURATION
# -----------------------------
# Read API keys and config from environment
MANATAL_API_KEY = os.getenv("MANATAL_API_KEY")
ASHBY_API_KEY = os.getenv("ASHBY_API_KEY")
PER_PAGE = int(os.getenv("PER_PAGE", 100))
API_SLEEP = float(os.getenv("API_SLEEP", 1))

LOG_FILE = "../logs/migration_log.csv"
CHECKPOINT_FILE = "../checkpoint.json"
RESUME_FOLDER = "../resumes"

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
os.makedirs(RESUME_FOLDER, exist_ok=True)

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def read_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f).get("last_id")
    return None

def save_checkpoint(last_id):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"last_id": last_id}, f)

def log_candidate(manatal_id, ashby_id, cv_status, notes_status, tags_status, error=""):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["manatal_id","ashby_id","cv","notes","tags","error"])
        writer.writerow([manatal_id, ashby_id, cv_status, notes_status, tags_status, error])

# -----------------------------
# MANATAL FUNCTIONS
# -----------------------------
def fetch_candidates(page=1):
    url = f"https://api.manatal.com/open/v3/candidates?page={page}&per_page={PER_PAGE}"
    headers = {"Authorization": f"Bearer {MANATAL_API_KEY}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def download_resume(url, candidate_id):
    if not url:
        return None
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_path = os.path.join(RESUME_FOLDER, f"{candidate_id}.pdf")
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    except Exception as e:
        print(f"Resume download failed for candidate {candidate_id}: {e}")
        return None

# -----------------------------
# ASHBY FUNCTIONS
# -----------------------------
def create_candidate_ashby(candidate):
    url = "https://api.ashbyhq.com/v1/candidates"
    headers = {"Authorization": f"Bearer {ASHBY_API_KEY}", "Content-Type": "application/json"}
    data = {
        "full_name": candidate["full_name"],
        "email": candidate["email"],
        "notes": candidate["notes"]
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()["id"]

def upload_resume_ashby(ashby_id, resume_file):
    if not resume_file:
        return False
    try:
        url = f"https://api.ashbyhq.com/v1/candidates/{ashby_id}/resume"
        headers = {"Authorization": f"Bearer {ASHBY_API_KEY}"}
        files = {"file": (os.path.basename(resume_file), open(resume_file, "rb"))}
        response = requests.post(url, files=files, headers=headers)
        return response.status_code == 200
    except Exception as e:
        print(f"Resume upload failed for Ashby ID {ashby_id}: {e}")
        return False

def add_tags_ashby(ashby_id, tags):
    # Placeholder: implement actual tag creation/assignment if Ashby API supports
    return True

# -----------------------------
# MAIN MIGRATION LOGIC
# -----------------------------
def map_candidate(manatal_candidate):
    return {
        "full_name": f"{manatal_candidate.get('first_name','')} {manatal_candidate.get('last_name','')}".strip(),
        "email": manatal_candidate.get("email"),
        "notes": manatal_candidate.get("notes",""),
        "tags": manatal_candidate.get("tags",[]),
        "resume_url": manatal_candidate.get("resume_url")
    }

def migrate():
    last_processed = read_checkpoint()
    page = 1
    while True:
        candidates = fetch_candidates(page)
        if not candidates:
            print("No more candidates to process.")
            break

        for manatal_candidate in candidates:
            manatal_id = manatal_candidate.get("id")
            if last_processed and manatal_id <= last_processed:
                continue

            candidate = map_candidate(manatal_candidate)
            try:
                ashby_id = create_candidate_ashby(candidate)

                # Resume upload
                cv_status = False
                if candidate["resume_url"]:
                    resume_file = download_resume(candidate["resume_url"], manatal_id)
                    cv_status = upload_resume_ashby(ashby_id, resume_file)

                notes_status = True if candidate["notes"] else False
                tags_status = add_tags_ashby(ashby_id, candidate["tags"])

                log_candidate(manatal_id, ashby_id, cv_status, notes_status, tags_status)
                save_checkpoint(manatal_id)
                print(f"Migrated candidate {manatal_id} → Ashby {ashby_id}")
                time.sleep(API_SLEEP)

            except Exception as e:
                print(f"Error migrating candidate {manatal_id}: {e}")
                log_candidate(manatal_id, "", False, False, False, str(e))

        page += 1

# -----------------------------
# RUN SCRIPT
# -----------------------------
if __name__ == "__main__":
    migrate()