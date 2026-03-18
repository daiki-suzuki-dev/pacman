def map_candidate(manatal_candidate):
    return {
        "full_name": f"{manatal_candidate.get('first_name','')} {manatal_candidate.get('last_name','')}".strip(),
        "email": manatal_candidate.get("email"),
        "notes": manatal_candidate.get("notes", ""),
        "tags": manatal_candidate.get("tags", []),
        "resume_url": manatal_candidate.get("resume_url")
    }