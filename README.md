# Journtasy

A top-down 2D dungeon crawler built with Python and Pygame. Navigate procedurally generated dungeons, fight enemies, and grow stronger as you level up your chosen character.

---

## Gameplay

- **Real-time combat** — Attack with left-click, move with WASD
- **Room exploration** — Walk off any screen edge to enter a new room
- **Character progression** — Defeat enemies to earn EXP and level up, scaling your health, damage, and armor
- **Pause / Resume** — Press `ESC` to pause at any time

---

## Features

### Characters
Choose from 6 playable characters, each with unique base stats and a dedicated weapon:

| Character | Health | Damage | Armor | Speed |
|-----------|--------|--------|-------|-------|
| Knight    | 180    | 40     | 14    | 20    |
| Monk      | —      | —      | —     | 5     |
| Killer    | —      | —      | —     | 5     |
| Wizard    | —      | —      | —     | 5     |
| Boxer     | —      | —      | —     | 5     |
| Caveman   | —      | —      | —     | 5     |

### Enemies
Three enemy tiers with escalating difficulty:

| Enemy   | Health | Damage | Armor |
|---------|--------|--------|-------|
| Type 1  | 75     | 14     | 3     |
| Type 2  | 120    | 20     | 7     |
| Type 3  | 170    | 27     | 11    |

Enemies patrol until aggroed (300-unit radius), then chase and attack the player. Defeated enemies drop experience scaled to their type and level.

### Dungeon Generation
- Rooms are procedurally generated and connected in all 4 directions
- Each room contains 1–5 randomly spawned enemies and 1–3 obstacles
- Backgrounds are randomly selected from 4 variants
- Entities spawn with overlap avoidance (up to 100 placement attempts)

### Combat
- Melee weapon attacks triggered by left-click
- Armor reduces incoming damage
- Player has a 30-frame invulnerability window after being hit
- Enemies have a 30-frame cooldown between attacks

### HUD
- **Health bar** — Displayed above every character
- **Experience bar** — Shows progress toward the next level
- **Level indicator** — Visible on all entities
- **Stats panel** — Live display of player health, damage, and armor (bottom-left)

---


## Getting Started

### Requirements
- Python 3.14
- [Pygame](https://pypi.org/project/pygame-ce/)

```bash
pip install pygame-ce
```

### Run

```bash
python main.py
```

---

## Controls

| Action       | Input       |
|--------------|-------------|
| Move         | `W A S D`   |
| Attack       | Left click  |
| Pause/Resume | `ESC`       |

---

## Architecture Highlights

- **Inheritance chain:** `Entity → AnimatedEntity → Character → Player / Enemy`
- **Manager pattern:** Dedicated managers for scenes, dungeon state, collisions, assets, and input
- **Stat system:** Modular `Health`, `Damage`, and `Armor` classes with level-scaling growth formulas
- **Generator pattern:** Each content type (enemies, obstacles, backgrounds) has its own generator
- **Centralized config:** All tunable values live in `scripts/config/constants.py`
