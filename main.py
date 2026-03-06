# main.py - Pac-Man Adventure
import pygame
import random
import math
import sys
import os

# Level maze data

LEVEL_LAYOUTS = [
    # Level 1 - Simple classic layout
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W............WW............W",
        "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
        "WoWWWW.WWWWW.WW.WWWWW.WWWWoW",
        "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
        "W..........................W",
        "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
        "W.WWWW.WW.WWWWWWWW.WW.WWWW.W",
        "W......WW....WW....WW......W",
        "WWWWWW.WWWWW WW WWWWW.WWWWWW",
        "WWWWWW.WWWWW WW WWWWW.WWWWWW",
        "WWWWWW.WW          WW.WWWWWW",
        "WWWWWW.WW WWWGGWWW WW.WWWWWW",
        "WWWWWW.WW W      W WW.WWWWWW",
        "      .   W      W   .      ",
        "WWWWWW.WW W      W WW.WWWWWW",
        "WWWWWW.WW WWWWWWWW WW.WWWWWW",
        "WWWWWW.WW          WW.WWWWWW",
        "WWWWWW.WW WWWWWWWW WW.WWWWWW",
        "WWWWWW.WW WWWWWWWW WW.WWWWWW",
        "W............WW............W",
        "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
        "W.WWWW.WWWWW.WW.WWWWW.WWWW.W",
        "Wo..WW................WW..oW",
        "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
        "WWW.WW.WW.WWWWWWWW.WW.WW.WWW",
        "W......WW....WW....WW......W",
        "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
        "W.WWWWWWWWWW.WW.WWWWWWWWWW.W",
        "W...........P............W.W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 2 - More complex layout
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W.........................oW",
        "W.WWWWWW.WWWWW.WWWWW.WWWWW.W",
        "W.WWWWWW.WWWWW.WWWWW.WWWWW.W",
        "W.WW.....WW....WW....WW....W",
        "W.WW.WWW.WW.WWWWW.WWWWW.WW.W",
        "W.WW.WWW.WW.WWWWW.WWWWW.WW.W",
        "W....WWW.............WWW...W",
        "WWWW.WWW.WWW.WWW.WWW.WWW.WWW",
        "WWWW.WWW.WWW.WWW.WWW.WWW.WWW",
        "W....WWW.WWW.....WWW.WWW...W",
        "W.WWWWWW.WWWWW.WWWWW.WWWWW.W",
        "W.WWWWWW.WWWWW.WWWWW.WWWWW.W",
        "Wo........G...P...G.......oW",
        "WWWWWWWW.WWWWW.WWWWW.WWWWWWW",
        "WWWWWWWW.WWWWW.WWWWW.WWWWWWW",
        "W.............W............W",
        "W.WWW.WWWWWWW.W.WWWWWWW.WWW.",
        "W.WWW.WWWWWWW.W.WWWWWWW.WWW.",
        "W.WWW.........W.........WWW.",
        "W.WWW.WWWWWWWWWWWWWWWWW.WWW.",
        "W.WWW.WWWWWWWWWWWWWWWWW.WWW.",
        "W.....WWWWWWWWWWWWWWWWW.....",
        "WWWWW.WWWWWWWWWWWWWWWWW.WWWW",
        "WWWWW.WWWWWWWWWWWWWWWWW.WWWW",
        "WWWWW...................WWWW",
        "WWWWWoWWWWWWWWWWWWWWWWWoWWWW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 3 - Spiral maze
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWWWWWWWWWWWWWWWWWWWWWW.W",
        "W.WP.......................W",
        "W.W.WWWWWWWWWWWWWWWWWWWWW.W",
        "W.W.W.....................W",
        "W.W.W.WWWWWWWWWWWWWWWWWW.W.W",
        "W.W.W.W...................W",
        "W.W.W.W.WWWWWWWWWWWWWWWW.W.W",
        "W.W.W.W.W.................W",
        "W.W.W.W.W.WWWWWWWWWWWWWW.W.W",
        "W.W.W.W.W.W...............W",
        "W.W.W.W.W.W.WWWWWWWWWWWW.W.W",
        "W.W.W.W.W.W.W....G.......W.W",
        "W.W.W.W.W.W.W.WWWWWWWWWW.W.W",
        "WGW.W.W.W.W.W.W.........W.W",
        "W...W.W.W.W.W.W.WWWWWWW.W.W",
        "WWW.W.W.W.W.W.W.W.....W.W.W",
        "W...W.W.W.W.W.W.WGW.W.W.W.W",
        "W.WWW.W.W.W.W.W...W.W.W.W.W",
        "W.....W.W.W.W.WWW.W.W.W.W.W",
        "WWWWWWW.W.W.W...W.W.W.W.W.W",
        "W.......W.W.WWW.W.W.W.W.W.W",
        "W.WWWWWWW.W...W.W.W.W.W.W.W",
        "W.........WWW.W.W.W.W.W...W",
        "WWWWWWWWWW....W.W.W.W.WWW.W",
        "Wo............W.W.W.W.....W",
        "WWWWWWWWWWWWWWW.W.W.WWWWWWW",
        "Wo..............W.........oW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 4 - Open center
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWW.WWWWW.WWWW.WWWWW.WW.W",
        "WoWWWW.WWWWW.WWWW.WWWWW.WWoW",
        "W.WWWW...WWW.WWWW.WWW...WW.W",
        "W......W....WWWWWW....W....W",
        "WWWWWW.WWWW........WWWW.WWWW",
        "WWWWWW.WWWWW.WWWW.WWWWW.WWWW",
        "WWWWWW.WWWWW.WWWW.WWWWW.WWWW",
        "WWWWWW.WW.............WW.WWWW",
        "WWWWWW.WW.WWWWWWWWWW.WW.WWWW",
        "WWWWWW.WW.WWWWWWWWWW.WW.WWWW",
        "WWWWWW.WW.WW      WW.WW.WWWW",
        "      .   WW      WW   .    ",
        "WWWWWW.WW WW  GG  WW WW.WWWW",
        "WWWWWW.WW WW  GG  WW WW.WWWW",
        "WWWWWW.WW WW      WW WW.WWWW",
        "WWWWWW.WW WWWWWWWWWW WW.WWWW",
        "WWWWWW.WW          P WW.WWWW",
        "WWWWWW.WW WWWWWWWWWWWWW.WWWW",
        "WWWWWW.WW WWWWWWWWWWWWW.WWWW",
        "W......WW.............WW...W",
        "W.WWWW.WWWWW.WWWW.WWWWW.WW.W",
        "W.WWWW.WWWWW.WWWW.WWWWW.WW.W",
        "Wo.WWW...........WWW...WWoW",
        "WWW.WWWWWWWWWWWWWWWWWWW.WWWW",
        "WWW..........................W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 5 - Checkerboard
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.........................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "Wo........................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...G.....................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...P.....G................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W.........................oW",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "Wo.........................W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 6 - Pathways
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWWWWWWWWWWWWWWWWWWWWWW.W",
        "W.W........................W",
        "W.W.WWWWWWWWWWWWWWWWWWWWWW.W",
        "W.W.W......................W",
        "W.W.W.WWWWWWWWWWWWWWWWWWWW.W",
        "W.W.W.W....................W",
        "W.W.W.W.WWWWWWWWWWWWWWWWWW.W",
        "W.W.W.W.W................W.W",
        "W.W.W.W.W.WWWWWWWWWWWWWW.W.W",
        "W.W.W.W.W.W...g..........W.W",
        "W.W.W.W.W.W.WWWWWW.WWWWW.W.W",
        "W.W.W.W.W.W.WP........GW.W.W",
        "W.W.W.W.W.W.WWW.WWWWWWWW.W.W",
        "W.W.W.W.W.W..............W.W",
        "W.W.W.W.W.WWWWWWWWWWWWWW.W.W",
        "W.W.W.W.W................W.W",
        "W.W.W.W.WWWWWWWWWWWWWWWW.W.W",
        "W.W.W.W..................W.W",
        "W.W.W.WWWWWWWWWWWWWWWWWW.W.W",
        "W.W.W.....................W.W",
        "W.W.WWWWWWWWWWWWWWWWWWWW.W.W",
        "W.W.......................W.W",
        "W.WWWWWWWWWWWWWWWWWWWWWW.W.W",
        "W.........................W.W",
        "WoWWWWWWWWWWWWWWWWWWWWWWWWoW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 7 - Chambers
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W...........W............W.W",
        "W.WWWWWWWWW.W.WWWWWWWWWW.W.W",
        "W.W.......W.W.W........W.W.W",
        "W.W.WWWWW.W.W.W.WWWWWW.W.W.W",
        "W.W.W...W.W.W.W.W....W.W.W.W",
        "W.W.W.W.W.W.W.W.W.WW.W.W.W.W",
        "W.W.W.W.W.W.W.W.W.WW.W.W.W.W",
        "W...W.W.W...W...W.WW.W...W.W",
        "WWWWW.W.WWWWWWWWW.WW.WWWWW.W",
        "Wo....W...........WW.....oW",
        "WWWWWWWWWWWWWWWWW.WWWWWWWWWW",
        "W.............W...W........W",
        "W.WWWWWWWWWWW.W.WWW.WWWWWW.W",
        "W.W...........W...W.W....W.W",
        "W.W.WWWWWWWWWWWWW.W.W.WW.W.W",
        "W.W.W.............W.W.WW.W.W",
        "W.W.W.WWWWWWWWWWWWW.W.WW.W.W",
        "W.W.W.W...........GW.WW.W.W",
        "W.W.W.W.WWWWWWWWWWW..WW.W.W",
        "W.W.W.W.WP..G........WW.W.W",
        "W.W.W.W.WWWWWWWWWWWWWWW.W.W",
        "W.W.W.W...............W.W.W",
        "W.W.W.WWWWWWWWWWWWWWW.W.W.W",
        "W.W.W.................W.W.W",
        "W.W.WWWWWWWWWWWWWWWWWWW.W.W",
        "W.W.......................W",
        "WoWWWWWWWWWWWWWWWWWWWWWWWWoW",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 8 - Scattered Walls
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W.................G........W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W..........................W",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "W..........................W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W.......................W..W",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "WP.........................W",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "W..........................W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W...G.....................W",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "WWW.WWWWW.WWWWW.WWWWW.WWW.WW",
        "W.........................oW",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "W.WWWW.WWWWW.WWWWW.WWWW.WW.W",
        "Wo.........................W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 9 - Zigzag
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.........................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "Wo........................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...G.....................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...P.....G................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W.........................oW",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "Wo.........................W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ],
    
    # Level 10 - Final Challenge
    [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.........................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "Wo........................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...G.....................oW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W..........................W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W...P.....G................W",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "WWWW.WWWW.WWWW.WWWW.WWWW.WWW",
        "W.........................oW",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "W.WWWW.WWWW.WWWW.WWWW.WWWW.W",
        "Wo.........................W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
]


TILE = 20
BOUNDARY = 30
WALL_W = 15
CARDINALS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIR_ANGLE = {(1, 0): 0, (0, 1): 90, (-1, 0): 180, (0, -1): 270}


def load_level(level_num):
    return LEVEL_LAYOUTS[level_num - 1] if 1 <= level_num <= len(LEVEL_LAYOUTS) else LEVEL_LAYOUTS[0]


class AnimatedBackground:
    def __init__(self, screen):
        self.screen = screen
        w, h = screen.get_width(), screen.get_height()
        self.dots = [{'x': random.randint(0, w), 'y': random.randint(0, h),
                      'dx': random.choice([-2, 2]), 'dy': random.choice([-2, 2]),
                      'alpha': random.randint(50, 255)} for _ in range(50)]

    def update(self):
        for d in self.dots:
            d['x'] += d['dx']; d['y'] += d['dy']
            if d['x'] <= 0 or d['x'] >= self.screen.get_width(): d['dx'] *= -1
            if d['y'] <= 0 or d['y'] >= self.screen.get_height(): d['dy'] *= -1
            d['alpha'] = (d['alpha'] + 5) % 255

    def draw(self):
        surf = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 180))
        for d in self.dots:
            pygame.draw.circle(surf, (0, 0, 255, d['alpha']), (int(d['x']), int(d['y'])), 4)
        self.screen.blit(surf, (0, 0))


class Button:
    def __init__(self, screen, text, pos, size, callback=None, param=None):
        self.screen, self.text, self.param = screen, text, param
        self.x, self.y = pos
        self.width, self.height = size
        self.callback, self.hovered = callback, False
        font = pygame.font.SysFont('Arial', 36)
        self.text_surf = font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))

    def draw(self):
        c = (255, 165, 0) if self.hovered else (255, 255, 0)
        pygame.draw.rect(self.screen, c, (self.x, self.y, self.width, self.height), 0, 10)
        pygame.draw.rect(self.screen, (0, 0, 255), (self.x, self.y, self.width, self.height), 2, 10)
        self.screen.blit(self.text_surf, self.text_rect)

    def check_hover(self, pos):
        prev, self.hovered = self.hovered, (self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height)
        return self.hovered != prev

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION: self.check_hover(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered and self.callback:
            self.callback(self.param if self.param is not None else ()); return True
        return False


class Menu:
    def __init__(self, screen, start_game_callback):
        self.screen, self.start_game_callback = screen, start_game_callback
        self.background = AnimatedBackground(screen)
        w, h = screen.get_width(), screen.get_height()
        bw, bh, sp = 250, 50, 20
        start_y = h // 4 + 50
        self.title_y, self.desc_y = h // 4 - 50, h // 4 + 50
        self.inst_y = h - 100
        self.buttons = []
        for row in range(2):
            for col in range(5):
                level = row * 5 + col + 1
                x = (w - (bw * 5 + sp * 4)) // 2 + col * (bw + sp)
                y = start_y + 100 + row * (bh + sp)
                self.buttons.append(Button(screen, f"Level {level}", (x, y), (bw, bh), start_game_callback, level))
        self.logo_font = pygame.font.SysFont('Arial', 96, bold=True)
        self.info_font = pygame.font.SysFont('Arial', 32)

    def update(self):
        self.background.update()
        for b in self.buttons: b.check_hover(pygame.mouse.get_pos())

    def handle_event(self, event):
        for b in self.buttons:
            if b.handle_event(event): return

    def draw(self):
        self.background.draw()
        w = self.screen.get_width()
        for surf, y in [(self.logo_font.render("PAC-MAN ADVENTURE", True, (255, 255, 0)), self.title_y),
                        (self.info_font.render("Navigate through mazes, eat dots, and avoid ghosts!", True, (255, 255, 255)), self.desc_y)]:
            self.screen.blit(surf, surf.get_rect(center=(w // 2, y)))
        for b in self.buttons: b.draw()
        inst = self.info_font.render("Use arrow keys to control Pac-Man. Press ESC to return to menu.", True, (200, 200, 200))
        self.screen.blit(inst, inst.get_rect(center=(w // 2, self.inst_y)))


def _can_move(rect, pos, walls):
    r = rect.copy(); r.x, r.y = pos[0], pos[1]
    return not any(r.colliderect(w) for w in walls)


class PacMan:
    def __init__(self, x, y, size):
        self.start_x, self.start_y, self.size, self.speed = x, y, size, 3
        self.mouth_angle, self.mouth_opening, self.anim_speed = 0, True, 10
        self.reset()

    def reset(self):
        self.rect = pygame.Rect(self.start_x, self.start_y, self.size, self.size)
        self.direction = self.next_direction = self.last_direction = (0, 0)
        self.moving = False
        self.position = [float(self.start_x), float(self.start_y)]
        self.last_position = self.position.copy()
        self.grid_x, self.grid_y = int(self.start_x / self.size), int(self.start_y / self.size)

    def set_direction(self, dx, dy): self.next_direction = (dx, dy); self.moving = True

    def update(self, walls):
        if self.next_direction != self.direction and self.moving:
            nx = self.position[0] + self.next_direction[0] * self.speed
            ny = self.position[1] + self.next_direction[1] * self.speed
            if _can_move(self.rect, (nx, ny), walls): self.direction = self.last_direction = self.next_direction
        if self.direction != (0, 0) and self.moving:
            nx = self.position[0] + self.direction[0] * self.speed
            ny = self.position[1] + self.direction[1] * self.speed
            if _can_move(self.rect, (nx, ny), walls):
                self.last_position = self.position.copy()
                self.position[0], self.position[1] = nx, ny
            else:
                self.position = self.last_position.copy()
                self.moving = False
                self.direction = self.next_direction = (0, 0)
        self.rect.x, self.rect.y = int(self.position[0]), int(self.position[1])
        self.grid_x, self.grid_y = int(self.position[0] / self.size), int(self.position[1] / self.size)
        if self.mouth_opening: self.mouth_angle = min(45, self.mouth_angle + self.anim_speed)
        else: self.mouth_angle = max(0, self.mouth_angle - self.anim_speed)
        if self.mouth_angle >= 45: self.mouth_opening = False
        elif self.mouth_angle <= 0: self.mouth_opening = True

    def draw(self, screen):
        c = (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)
        pygame.draw.circle(screen, (255, 255, 0), c, self.rect.width // 2)
        if self.direction != (0, 0):
            a = math.radians(DIR_ANGLE.get(self.direction, 0))
            pygame.draw.polygon(screen, (0, 0, 0), [c,
                (c[0] + math.cos(a - math.radians(self.mouth_angle)) * self.rect.width // 2, c[1] + math.sin(a - math.radians(self.mouth_angle)) * self.rect.width // 2),
                (c[0] + math.cos(a + math.radians(self.mouth_angle)) * self.rect.width // 2, c[1] + math.sin(a + math.radians(self.mouth_angle)) * self.rect.width // 2)])


def _cardinal_toward(rect, target_rect, toward=True):
    dx = (target_rect.centerx - rect.centerx) * (1 if toward else -1)
    dy = (target_rect.centery - rect.centery) * (1 if toward else -1)
    length = max(0.1, math.sqrt(dx * dx + dy * dy))
    dx, dy = dx / length, dy / length
    return (1 if dx > 0 else -1, 0) if abs(dx) > abs(dy) else (0, 1 if dy > 0 else -1)


class Ghost:
    def __init__(self, x, y, size, color):
        self.start_x, self.start_y, self.size, self.color = x, y, size, color
        self.scared_color = (0, 0, 255)
        self.behavior = random.choice(["chase", "random", "patrol"])
        self.patrol_pts = [(random.randint(100, 700), random.randint(100, 500)) for _ in range(4)]
        self.cur_patrol = 0
        self.reset()

    def reset(self): self.rect = pygame.Rect(self.start_x, self.start_y, self.size, self.size); self.direction = (0, 0); self.speed = 0.8

    def update(self, walls, pacman, scared=False):
        sp = self.speed * 0.3 if scared else self.speed
        if scared: self.direction = _cardinal_toward(self.rect, pacman.rect, False)
        elif self.behavior == "chase": self.direction = _cardinal_toward(self.rect, pacman.rect, True)
        elif self.behavior == "random" and random.random() < 0.02: self.direction = random.choice(CARDINALS)
        elif self.behavior == "patrol" and self.patrol_pts:
            t = self.patrol_pts[self.cur_patrol]
            dx, dy = t[0] - self.rect.centerx, t[1] - self.rect.centery
            if abs(dx) < 10 and abs(dy) < 10: self.cur_patrol = (self.cur_patrol + 1) % len(self.patrol_pts)
            else: self.direction = _cardinal_toward(self.rect, pygame.Rect(t[0], t[1], 1, 1), True)
        nr = self.rect.copy(); nr.x += self.direction[0] * sp; nr.y += self.direction[1] * sp
        if not any(nr.colliderect(w) for w in walls): self.rect = nr
        else:
            for d in random.sample(CARDINALS, len(CARDINALS)):
                nr = self.rect.copy(); nr.x += d[0] * self.speed; nr.y += d[1] * self.speed
                if not any(nr.colliderect(w) for w in walls): self.direction = d; break

    def draw(self, screen, scared=False):
        color = self.scared_color if scared else self.color
        ey = self.rect.centery - self.size // 4
        pygame.draw.circle(screen, color, (self.rect.centerx, ey), self.size // 2)
        pygame.draw.rect(screen, color, (self.rect.x, ey, self.size, self.size // 2))
        for i in range(3): pygame.draw.circle(screen, (0, 0, 0), (self.rect.x + (i + 0.5) * (self.size // 3), self.rect.bottom), self.size // 6)
        es = self.size // 5
        for ox in (-es, es): pygame.draw.circle(screen, (255, 255, 255), (self.rect.centerx + ox, ey), es)
        pu = (self.rect.centerx + self.direction[0] * es // 2, ey + self.direction[1] * es // 2)
        for ox in (-es, es): pygame.draw.circle(screen, (0, 0, 0) if scared else (0, 0, 255), (self.rect.centerx + ox + (0 if scared else self.direction[0] * es // 2), ey + (0 if scared else self.direction[1] * es // 2)), es // 2)


class Pellet:
    def __init__(self, x, y, tile_size, power=False):
        s = (tile_size // 2 if power else tile_size // 5)
        self.rect = pygame.Rect(x + tile_size // 2 - s // 2, y + tile_size // 2 - s // 2, s, s)
        self.power, self.flash = power, 0

    def draw(self, screen):
        if self.power:
            self.flash += 1
            if self.flash >= 30: self.flash = 0
            if self.flash >= 15: return
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, self.rect.width // 2)


class Game:
    WALL_COLORS = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 165, 0), (128, 0, 128), (0, 128, 0), (255, 192, 203)]
    KEY_DIR = {pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}

    def __init__(self, screen, level_num, level_done, game_over):
        self.screen, self.level_num = screen, level_num
        self.level_done, self.game_over = level_done, game_over
        self.score, self.lives, self.paused = 0, 3, False
        self.map_data = load_level(level_num)
        mw, mh = len(self.map_data[0]) * TILE, len(self.map_data) * TILE
        self.map_ox = (screen.get_width() - mw) // 2
        self.map_oy = (screen.get_height() - mh) // 2
        self.create_entities(mw, mh)
        self.font = pygame.font.SysFont('Arial', 24)
        self.game_active, self.power_active, self.power_timer = True, False, 0

    def create_entities(self, mw, mh):
        self.pacman, self.ghosts, self.pellets, self.power_pellets = None, [], [], []
        ghost_colors = [(255, 0, 0), (255, 184, 255), (0, 255, 255), (255, 184, 82)]
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                sx, sy = self.map_ox + x * TILE, self.map_oy + y * TILE
                if cell == 'P': self.pacman = PacMan(sx, sy, TILE)
                elif cell in ('G', 'g'): self.ghosts.append(Ghost(sx, sy, TILE, ghost_colors[len(self.ghosts) % 4]))
                elif cell == '.': self.pellets.append(Pellet(sx, sy, TILE, False))
                elif cell in ('O', 'o'): self.power_pellets.append(Pellet(sx, sy, TILE, True))
        self.wall_rects = [
            pygame.Rect(self.map_ox - BOUNDARY, self.map_oy - BOUNDARY, mw + 2 * BOUNDARY, WALL_W),
            pygame.Rect(self.map_ox - BOUNDARY, self.map_oy + mh + BOUNDARY - WALL_W, mw + 2 * BOUNDARY, WALL_W),
            pygame.Rect(self.map_ox - BOUNDARY, self.map_oy - BOUNDARY, WALL_W, mh + 2 * BOUNDARY),
            pygame.Rect(self.map_ox + mw + BOUNDARY - WALL_W, self.map_oy - BOUNDARY, WALL_W, mh + 2 * BOUNDARY)
        ]
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                if cell == 'W':
                    self.wall_rects.append(pygame.Rect(self.map_ox + x * TILE + 2.5, self.map_oy + y * TILE + 2.5, WALL_W, WALL_W))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: self.paused = not self.paused
            elif self.pacman and not self.paused and event.key in self.KEY_DIR: self.pacman.set_direction(*self.KEY_DIR[event.key])
        elif event.type == pygame.KEYUP and self.pacman and not self.paused and event.key in self.KEY_DIR:
            if self.pacman.direction == self.KEY_DIR[event.key]: self.pacman.set_direction(0, 0); self.pacman.moving = False

    def update(self):
        if self.paused or not self.game_active: return
        if self.pacman:
            self.pacman.update(self.wall_rects)
            for p in self.pellets[:]:
                if self.pacman.rect.colliderect(p.rect): self.pellets.remove(p); self.score += 10
            for p in self.power_pellets[:]:
                if self.pacman.rect.colliderect(p.rect): self.power_pellets.remove(p); self.score += 50; self.power_active = True; self.power_timer = 300
            for g in self.ghosts:
                if self.pacman.rect.colliderect(g.rect):
                    if self.power_active: g.reset(); self.score += 200
                    else:
                        self.lives -= 1
                        if self.lives <= 0: self.game_active = False; self.game_over(self.score)
                        else: self.pacman.reset(); [x.reset() for x in self.ghosts]
        scared = self.power_active and (self.power_timer >= 60 or self.power_timer % 10 < 5)
        for g in self.ghosts: g.update(self.wall_rects, self.pacman, scared)
        if self.power_active: self.power_timer -= 1; self.power_active = self.power_timer > 0
        if not self.pellets and not self.power_pellets: self.game_active = False; self.level_done(self.score)

    def draw(self):
        wc = self.WALL_COLORS[self.level_num - 1]
        for w in self.wall_rects: pygame.draw.rect(self.screen, wc, w)
        for p in self.pellets: p.draw(self.screen)
        for p in self.power_pellets: p.draw(self.screen)
        for g in self.ghosts: g.draw(self.screen, self.power_active)
        if self.pacman: self.pacman.draw(self.screen)
        for i, t in enumerate([(f"Score: {self.score}", 20), (f"Lives: {self.lives}", 50), (f"Level: {self.level_num}", 80)]):
            self.screen.blit(self.font.render(t[0], True, (255, 255, 255)), (20, t[1]))
        if self.paused:
            pt = pygame.font.SysFont('Arial', 48).render("PAUSED", True, (255, 255, 255))
            self.screen.blit(pt, pt.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2)))


# --- Main ---
pygame.init()
pygame.font.init()
SCREEN_W, SCREEN_H = 1400, 800
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Pac-Man Adventure")
clock = pygame.time.Clock()
MENU, PLAYING, GAME_OVER, LEVEL_COMPLETE = 0, 1, 2, 3


class PacManGame:
    def __init__(self):
        self.screen, self.clock = screen, clock
        self.state, self.level, self.score = MENU, 1, 0
        self.menu = Menu(screen, self.start_game)
        self.game = None

    def start_game(self, level=1):
        self.level = level
        self.game = Game(screen, level, self.end_level, self.game_over_cb)
        self.state = PLAYING

    def end_level(self, score):
        self.score += score; self.level += 1
        self.state = MENU if self.level > 10 else LEVEL_COMPLETE
        if self.level > 10: self.level = 1

    def game_over_cb(self, score): self.score += score; self.state = GAME_OVER

    def run(self):
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT: running = False
                if self.state == MENU: self.menu.handle_event(e)
                elif self.state == PLAYING: self.game.handle_event(e)
                elif self.state == GAME_OVER and e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN: self.state = MENU
                elif self.state == LEVEL_COMPLETE and e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN: self.start_game(self.level)
            if self.state == MENU: self.menu.update()
            elif self.state == PLAYING: self.game.update()
            self.screen.fill((0, 0, 0))
            if self.state == MENU: self.menu.draw()
            elif self.state == PLAYING: self.game.draw()
            elif self.state == GAME_OVER:
                f = pygame.font.SysFont('Arial', 48)
                for i, (txt, color) in enumerate([('GAME OVER', (255, 0, 0)), (f'Score: {self.score}', (255, 255, 255)), ('Press Enter to continue', (255, 255, 255))]):
                    s = f.render(txt, True, color)
                    self.screen.blit(s, (SCREEN_W // 2 - s.get_width() // 2, SCREEN_H // 2 - 100 + i * 100))
            elif self.state == LEVEL_COMPLETE:
                f = pygame.font.SysFont('Arial', 48)
                for i, txt in enumerate([f'Level {self.level - 1} Complete!', f'Score: {self.score}', 'Press Enter to continue to next level']):
                    s = f.render(txt, True, (255, 255, 0) if i == 0 else (255, 255, 255))
                    self.screen.blit(s, (SCREEN_W // 2 - s.get_width() // 2, SCREEN_H // 2 - 100 + i * 100))
            pygame.display.flip(); self.clock.tick(60)
        pygame.quit(); sys.exit()


if __name__ == "__main__":
    PacManGame().run()
