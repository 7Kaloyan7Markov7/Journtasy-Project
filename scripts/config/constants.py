TOP_LEFT_CORNER = (0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FIRST_LEVEL = 1

SCREEN_UPPER_BOUNDARY = 0
SCREEN_LEFT_BOUNDARY = 0
SCREEN_LOWER_BOUNDARY = 600
SCREEN_RIGHT_BOUNDARY = 800

# =========================
# SCENES
# =========================

GAME_SCENE_ID = "GAMESCENE"
MAIN_MENU_ID = "MAINMENU"

# =========================
# BACKGROUNDS
# =========================

FIRST_BACKGROUND_ID = "1b"
SECOND_BACKGROUND_ID = "2b"
THIRD_BACKGROUND_ID = "3b"
FOURTH_BACKGROUND_ID = "4b"

BACKGROUND_IDS = [
    FIRST_BACKGROUND_ID,
    SECOND_BACKGROUND_ID,
    THIRD_BACKGROUND_ID,
    FOURTH_BACKGROUND_ID,
]

BACKGROUND_PATHS = {
    FIRST_BACKGROUND_ID: "assets/backgrounds/background_grass.png",
    SECOND_BACKGROUND_ID: "assets/backgrounds/background_grass_dark.png",
    THIRD_BACKGROUND_ID: "assets/backgrounds/background_bricks.png",
    FOURTH_BACKGROUND_ID: "assets/backgrounds/background_panel.png",
}

BACKGROUND_SCALE = 3

# =========================
# PROJECTILES
# =========================

PROJECTILE_FRAME_SPACE = 10
PROJECTILE_FRAME_COUNT = 10
PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 10
PROJECTILE_SCALE = 3

FIRST_PROJECTILE_ID = "1p"
SECOND_PROJECTILE_ID = "2p"
THIRD_PROJECTILE_ID = "3p"

PROJECTILE_IDS = [
    FIRST_PROJECTILE_ID,
    SECOND_PROJECTILE_ID,
    THIRD_PROJECTILE_ID,
]

PROJECTILE_SPRITE_FILES = {
    FIRST_PROJECTILE_ID: [
        "assets/sprites/projectile_sprites/projectile1_sprites/projectile1_down.png",
        "assets/sprites/projectile_sprites/projectile1_sprites/projectile1_up.png",
        "assets/sprites/projectile_sprites/projectile1_sprites/projectile1_left.png",
        "assets/sprites/projectile_sprites/projectile1_sprites/projectile1_right.png",
    ],
    SECOND_PROJECTILE_ID: [
        "assets/sprites/projectile_sprites/projectile2_sprites/projectile2_down.png",
        "assets/sprites/projectile_sprites/projectile2_sprites/projectile2_up.png",
        "assets/sprites/projectile_sprites/projectile2_sprites/projectile2_left.png",
        "assets/sprites/projectile_sprites/projectile2_sprites/projectile2_right.png",
    ],
    THIRD_PROJECTILE_ID: [
        "assets/sprites/projectile_sprites/projectile3_sprites/projectile3_down.png",
        "assets/sprites/projectile_sprites/projectile3_sprites/projectile3_up.png",
        "assets/sprites/projectile_sprites/projectile3_sprites/projectile3_left.png",
        "assets/sprites/projectile_sprites/projectile3_sprites/projectile3_right.png",
    ],
}

# =========================
# PLAYERS SPRITES
# =========================

PLAYER_SPRITE_HEIGHT = 32
PLAYER_SPRITE_WIDTH = 18
PLAYER_FRAME_COUNT = 5
PLAYER_FRAME_SPACE = 14
PLAYER_SCALE = 4

KNIGHT_ID = "!K"
MONK_ID = "!M"
KILLER_ID = "!I"
WIZARD_ID = "!W"
BOXER_ID = "!B"
CAVEMAN_ID = "!C"

PLAYABLE_CHARACTER_IDS = [
    KNIGHT_ID,
    MONK_ID,
    KILLER_ID,
    WIZARD_ID,
    BOXER_ID,
    CAVEMAN_ID
]

PLAYER_SPRITE_FILES = {
    KNIGHT_ID: [
        "assets/sprites/player_sprites/knight_sprites/knight_down_sprites.png",
        "assets/sprites/player_sprites/knight_sprites/knight_up_sprites.png",
        "assets/sprites/player_sprites/knight_sprites/knight_left_sprites.png",
        "assets/sprites/player_sprites/knight_sprites/knight_right_sprites.png",
    ],
    MONK_ID: [
        "assets/sprites/player_sprites/monk_sprites/monk_down_sprites.png",
        "assets/sprites/player_sprites/monk_sprites/monk_up_sprites.png",
        "assets/sprites/player_sprites/monk_sprites/monk_left_sprites.png",
        "assets/sprites/player_sprites/monk_sprites/monk_right_sprites.png",
    ],
    KILLER_ID: [
        "assets/sprites/player_sprites/killer_sprites/killer_down_sprites.png",
        "assets/sprites/player_sprites/killer_sprites/killer_up_sprites.png",
        "assets/sprites/player_sprites/killer_sprites/killer_left_sprites.png",
        "assets/sprites/player_sprites/killer_sprites/killer_right_sprites.png",
    ],
    WIZARD_ID: [
        "assets/sprites/player_sprites/wizard_sprites/wizard_down_sprites.png",
        "assets/sprites/player_sprites/wizard_sprites/wizard_up_sprites.png",
        "assets/sprites/player_sprites/wizard_sprites/wizard_left_sprites.png",
        "assets/sprites/player_sprites/wizard_sprites/wizard_right_sprites.png",
    ],
    BOXER_ID: [
        "assets/sprites/player_sprites/boxer_sprites/boxer_down_sprites.png",
        "assets/sprites/player_sprites/boxer_sprites/boxer_up_sprites.png",
        "assets/sprites/player_sprites/boxer_sprites/boxer_left_sprites.png",
        "assets/sprites/player_sprites/boxer_sprites/boxer_right_sprites.png",
    ],
    CAVEMAN_ID: [
        "assets/sprites/player_sprites/caveman_sprites/caveman_down_sprites.png",
        "assets/sprites/player_sprites/caveman_sprites/caveman_up_sprites.png",
        "assets/sprites/player_sprites/caveman_sprites/caveman_left_sprites.png",
        "assets/sprites/player_sprites/caveman_sprites/caveman_right_sprites.png",
    ],
}

# =========================
# ENEMIES
# =========================

ENEMY_FRAME_SPACE = 27
ENEMY_FRAME_COUNT = 6
ENEMY_WIDTH = 37
ENEMY_HEIGHT = 33
ENEMY_SCALE = 3

FIRST_ENEMY_ID = "1e"
SECOND_ENEMY_ID = "2e"
THIRD_ENEMY_ID = "3e"

ENEMY_IDS = [
    FIRST_ENEMY_ID,
    SECOND_ENEMY_ID,
    THIRD_ENEMY_ID,
]

ENEMY_SPRITE_FILES = {
    FIRST_ENEMY_ID: [
        "assets/sprites/enemy_sprites/enemy1_sprite/enemy1_down_sprite.png",
        "assets/sprites/enemy_sprites/enemy1_sprite/enemy1_up_sprite.png",
        "assets/sprites/enemy_sprites/enemy1_sprite/enemy1_left_sprite.png",
        "assets/sprites/enemy_sprites/enemy1_sprite/enemy1_right_sprite.png",
    ],
    SECOND_ENEMY_ID: [
        "assets/sprites/enemy_sprites/enemy2_sprite/enemy2_down_sprite.png",
        "assets/sprites/enemy_sprites/enemy2_sprite/enemy2_up_sprite.png",
        "assets/sprites/enemy_sprites/enemy2_sprite/enemy2_left_sprite.png",
        "assets/sprites/enemy_sprites/enemy2_sprite/enemy2_right_sprite.png",
    ],
    THIRD_ENEMY_ID: [
        "assets/sprites/enemy_sprites/enemy3_sprite/enemy3_down_sprite.png",
        "assets/sprites/enemy_sprites/enemy3_sprite/enemy3_up_sprite.png",
        "assets/sprites/enemy_sprites/enemy3_sprite/enemy3_left_sprite.png",
        "assets/sprites/enemy_sprites/enemy3_sprite/enemy3_right_sprite.png",
    ],
}

# =========================
# OBSTACLES
# =========================

ZERO_SPEED = 0

OBSTACLE_FRAME_SPACE = 1
OBSTACLE_FRAME_COUNT = 1
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 60
OBSTACLE_SCALE = 1

FIRST_OBSTACLE_ID = "1o"
SECOND_OBSTACLE_ID = "2o"
THIRD_OBSTACLE_ID = "3o"

OBSTACLE_IDS = [
    FIRST_OBSTACLE_ID,
    SECOND_OBSTACLE_ID,
    THIRD_OBSTACLE_ID,
]

OBSTACLE_IMAGE_FILES = {
    FIRST_OBSTACLE_ID: "assets/obstacles/obstacle_1.png",
    SECOND_OBSTACLE_ID: "assets/obstacles/obstacle_2.png",
    THIRD_OBSTACLE_ID: "assets/obstacles/obstacle_3.png",
}

# =========================
# WEAPONS
# =========================

WEAPON_FRAME_SPACE = 0
WEAPON_FRAME_COUNT = 5
WEAPON_WIDTH = 27
WEAPON_HEIGHT = 32
WEAPON_SCALE = 5

KNIGHT_WEAPON_ID = "!K_w"
MONK_WEAPON_ID = "!M_w"
KILLER_WEAPON_ID = "!I_w"
WIZARD_WEAPON_ID = "!W_w"
BOXER_WEAPON_ID = "!B_w"
CAVEMAN_WEAPON_ID = "!C_w"

WEAPON_IDS = [
    KNIGHT_WEAPON_ID,
    MONK_WEAPON_ID,
    KILLER_WEAPON_ID,
    WIZARD_WEAPON_ID,
    BOXER_WEAPON_ID,
    CAVEMAN_WEAPON_ID,
]

WEAPON_SPRITE_FILES = {
    KNIGHT_ID: ["assets/sprites/weapon_sprites/knight_weapon/knight_weapon_left.png", "assets/sprites/weapon_sprites/knight_weapon/knight_weapon_right.png"],
    MONK_ID: ["assets/sprites/weapon_sprites/monk_weapon/monk_weapon_left.png", "assets/sprites/weapon_sprites/monk_weapon/monk_weapon_right.png"],
    KILLER_ID: ["assets/sprites/weapon_sprites/killer_weapon/killer_weapon_left.png", "assets/sprites/weapon_sprites/killer_weapon/killer_weapon_right.png"],
    WIZARD_ID: ["assets/sprites/weapon_sprites/wizard_weapon/wizard_weapon_left.png", "assets/sprites/weapon_sprites/wizard_weapon/wizard_weapon_right.png"],
    BOXER_ID: ["assets/sprites/weapon_sprites/boxer_weapon/boxer_weapon_left.png", "assets/sprites/weapon_sprites/boxer_weapon/boxer_weapon_right.png"],
    CAVEMAN_ID: ["assets/sprites/weapon_sprites/caveman_weapon/caveman_weapon_left.png", "assets/sprites/weapon_sprites/caveman_weapon/caveman_weapon_right.png"],
}

# =========================
# GENERAL
# =========================

SIXTY_FPS = 60

# =========================
# STATS KEYS
# =========================

HEALTH = "health"
ARMOR = "armor"
DAMAGE = "damage"

# =========================
# PLAYER STATS
# =========================

KNIGHT_BASE_HEALTH = 180
KNIGHT_HEALTH_GROWTH = 22
KNIGHT_BASE_DAMAGE = 28
KNIGHT_DAMAGE_GROWTH = 4
KNIGHT_BASE_ARMOR = 14
KNIGHT_ARMOR_GROWTH = 3
KNIGHT_HEALING = 0

MONK_BASE_HEALTH = 0
MONK_HEALTH_GROWTH = 0
MONK_BASE_DAMAGE = 0
MONK_DAMAGE_GROWTH = 0
MONK_BASE_ARMOR = 0
MONK_ARMOR_GROWTH = 0
MONK_HEALING = 0

KILLER_BASE_HEALTH = 0
KILLER_HEALTH_GROWTH = 0
KILLER_BASE_DAMAGE = 0
KILLER_DAMAGE_GROWTH = 0
KILLER_BASE_ARMOR = 0
KILLER_ARMOR_GROWTH = 0
KILLER_HEALING = 0

WIZARD_BASE_HEALTH = 0
WIZARD_HEALTH_GROWTH = 0
WIZARD_BASE_DAMAGE = 0
WIZARD_DAMAGE_GROWTH = 0
WIZARD_BASE_ARMOR = 0
WIZARD_ARMOR_GROWTH = 0
WIZARD_HEALING = 0

BOXER_BASE_HEALTH = 0
BOXER_HEALTH_GROWTH = 0
BOXER_BASE_DAMAGE = 0
BOXER_DAMAGE_GROWTH = 0
BOXER_BASE_ARMOR = 0
BOXER_ARMOR_GROWTH = 0
BOXER_HEALING = 0

CAVEMAN_BASE_HEALTH = 0
CAVEMAN_HEALTH_GROWTH = 0
CAVEMAN_BASE_DAMAGE = 0
CAVEMAN_DAMAGE_GROWTH = 0
CAVEMAN_BASE_ARMOR = 0
CAVEMAN_ARMOR_GROWTH = 0
CAVEMAN_HEALING = 0

# =========================
# ENEMY STATS
# =========================

FIRST_ENEMY_BASE_HEALTH = 75
FIRST_ENEMY_HEALTH_GROWTH = 9
FIRST_ENEMY_BASE_ARMOR = 3
FIRST_ENEMY_ARMOR_GROWTH = 1
FIRST_ENEMY_BASE_DAMAGE = 14
FIRST_ENEMY_DAMAGE_GROWTH = 2
FIRST_ENEMY_HEALING = 0
FIRST_ENEMY_EXP = 10
FIRST_ENEMY_EXP_GROWTH = 0.4

SECOND_ENEMY_BASE_HEALTH = 120
SECOND_ENEMY_HEALTH_GROWTH = 13
SECOND_ENEMY_BASE_ARMOR = 7
SECOND_ENEMY_ARMOR_GROWTH = 2
SECOND_ENEMY_BASE_DAMAGE = 20
SECOND_ENEMY_DAMAGE_GROWTH = 3
SECOND_ENEMY_HEALING = 0
SECOND_ENEMY_EXP = 15
SECOND_ENEMY_EXP_GROWTH = 0.6

THIRD_ENEMY_BASE_HEALTH = 170
THIRD_ENEMY_HEALTH_GROWTH = 17
THIRD_ENEMY_BASE_ARMOR = 11
THIRD_ENEMY_ARMOR_GROWTH = 3
THIRD_ENEMY_BASE_DAMAGE = 27
THIRD_ENEMY_DAMAGE_GROWTH = 4
THIRD_ENEMY_HEALING = 0
THIRD_ENEMY_EXP = 20
THIRD_ENEMY_EXP_GROWTH = 0.8

ENEMY_EXP_DROPS = {FIRST_ENEMY_ID : [FIRST_ENEMY_EXP, FIRST_ENEMY_EXP_GROWTH],
                   SECOND_ENEMY_ID : [SECOND_ENEMY_EXP, SECOND_ENEMY_EXP_GROWTH],
                   THIRD_ENEMY_ID : [THIRD_ENEMY_EXP, THIRD_ENEMY_EXP_GROWTH]}

# =========================
# CHARACTER STATS MAP
# =========================

CHARACTER_STATS = {
    KNIGHT_ID: {
        HEALTH: [KNIGHT_BASE_HEALTH, KNIGHT_HEALTH_GROWTH, KNIGHT_HEALING],
        ARMOR: [KNIGHT_BASE_ARMOR, KNIGHT_ARMOR_GROWTH],
        DAMAGE: [KNIGHT_BASE_DAMAGE, KNIGHT_DAMAGE_GROWTH],
    },
    MONK_ID: {
        HEALTH: [MONK_BASE_HEALTH, MONK_HEALTH_GROWTH, MONK_HEALING],
        ARMOR: [MONK_BASE_ARMOR, MONK_ARMOR_GROWTH],
        DAMAGE: [MONK_BASE_DAMAGE, MONK_DAMAGE_GROWTH],
    },
    KILLER_ID: {
        HEALTH: [KILLER_BASE_HEALTH, KILLER_HEALTH_GROWTH, KILLER_HEALING],
        ARMOR: [KILLER_BASE_ARMOR, KILLER_ARMOR_GROWTH],
        DAMAGE: [KILLER_BASE_DAMAGE, KILLER_DAMAGE_GROWTH],
    },
    WIZARD_ID: {
        HEALTH: [WIZARD_BASE_HEALTH, WIZARD_HEALTH_GROWTH, WIZARD_HEALING],
        ARMOR: [WIZARD_BASE_ARMOR, WIZARD_ARMOR_GROWTH],
        DAMAGE: [WIZARD_BASE_DAMAGE, WIZARD_DAMAGE_GROWTH],
    },
    BOXER_ID: {
        HEALTH: [BOXER_BASE_HEALTH, BOXER_HEALTH_GROWTH, BOXER_HEALING],
        ARMOR: [BOXER_BASE_ARMOR, BOXER_ARMOR_GROWTH],
        DAMAGE: [BOXER_BASE_DAMAGE, BOXER_DAMAGE_GROWTH],
    },
    CAVEMAN_ID: {
        HEALTH: [CAVEMAN_BASE_HEALTH, CAVEMAN_HEALTH_GROWTH, CAVEMAN_HEALING],
        ARMOR: [CAVEMAN_BASE_ARMOR, CAVEMAN_ARMOR_GROWTH],
        DAMAGE: [CAVEMAN_BASE_DAMAGE, CAVEMAN_DAMAGE_GROWTH],
    },
    FIRST_ENEMY_ID: {
        HEALTH: [FIRST_ENEMY_BASE_HEALTH, FIRST_ENEMY_HEALTH_GROWTH, FIRST_ENEMY_HEALING],
        ARMOR: [FIRST_ENEMY_BASE_ARMOR, FIRST_ENEMY_ARMOR_GROWTH],
        DAMAGE: [FIRST_ENEMY_BASE_DAMAGE, FIRST_ENEMY_DAMAGE_GROWTH],
    },
    SECOND_ENEMY_ID: {
        HEALTH: [SECOND_ENEMY_BASE_HEALTH, SECOND_ENEMY_HEALTH_GROWTH, SECOND_ENEMY_HEALING],
        ARMOR: [SECOND_ENEMY_BASE_ARMOR, SECOND_ENEMY_ARMOR_GROWTH],
        DAMAGE: [SECOND_ENEMY_BASE_DAMAGE, SECOND_ENEMY_DAMAGE_GROWTH],
    },
    THIRD_ENEMY_ID: {
        HEALTH: [THIRD_ENEMY_BASE_HEALTH, THIRD_ENEMY_HEALTH_GROWTH, THIRD_ENEMY_HEALING],
        ARMOR: [THIRD_ENEMY_BASE_ARMOR, THIRD_ENEMY_ARMOR_GROWTH],
        DAMAGE: [THIRD_ENEMY_BASE_DAMAGE, THIRD_ENEMY_DAMAGE_GROWTH],
    },
}

# =========================
# FAMILY IDS
# =========================

PLAYER_ID = "!"
WEAPON_ID = "w"
ENEMY_ID = "e"
OBSTACLE_ID = "o"
PROJECTILE_ID = "p"

# =========================
# HITBOX DATA
# =========================

PLAYER_HITBOX = [PLAYER_SPRITE_WIDTH * PLAYER_SCALE, PLAYER_SPRITE_HEIGHT * PLAYER_SCALE]

WEAPON_HITBOX_DATA = {
    KNIGHT_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
    MONK_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
    KILLER_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
    WIZARD_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
    BOXER_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
    CAVEMAN_WEAPON_ID: [WEAPON_WIDTH * WEAPON_SCALE, WEAPON_HEIGHT * WEAPON_SCALE],
}

ENEMY_HITBOX_DATA = {
    FIRST_ENEMY_ID: [ENEMY_WIDTH * ENEMY_SCALE, ENEMY_HEIGHT * ENEMY_SCALE],
    SECOND_ENEMY_ID: [ENEMY_WIDTH * ENEMY_SCALE, ENEMY_HEIGHT * ENEMY_SCALE],
    THIRD_ENEMY_ID: [ENEMY_WIDTH * ENEMY_SCALE, ENEMY_HEIGHT * ENEMY_SCALE],
}

OBSTACLE_HITBOX_DATA = {
    FIRST_OBSTACLE_ID: [OBSTACLE_WIDTH * OBSTACLE_SCALE, OBSTACLE_HEIGHT * OBSTACLE_SCALE],
    SECOND_OBSTACLE_ID: [OBSTACLE_WIDTH * OBSTACLE_SCALE, OBSTACLE_HEIGHT * OBSTACLE_SCALE],
    THIRD_OBSTACLE_ID: [OBSTACLE_WIDTH * OBSTACLE_SCALE, OBSTACLE_HEIGHT * OBSTACLE_SCALE],
}

PROJECTILE_HITBOX_DATA = {
    FIRST_PROJECTILE_ID: [PROJECTILE_WIDTH * PROJECTILE_SCALE, PROJECTILE_HEIGHT * PROJECTILE_SCALE],
    SECOND_PROJECTILE_ID: [PROJECTILE_WIDTH * PROJECTILE_SCALE, PROJECTILE_HEIGHT * PROJECTILE_SCALE],
    THIRD_PROJECTILE_ID: [PROJECTILE_WIDTH * PROJECTILE_SCALE, PROJECTILE_HEIGHT * PROJECTILE_SCALE],
}

HITBOX_DATA = {
    PLAYER_ID: PLAYER_HITBOX,
    WEAPON_ID: WEAPON_HITBOX_DATA,
    ENEMY_ID: ENEMY_HITBOX_DATA,
    OBSTACLE_ID: OBSTACLE_HITBOX_DATA,
    PROJECTILE_ID: PROJECTILE_HITBOX_DATA,
}

# =========================
# PLAYER_IDS MAPPED TO WEAPON_IDS
# =========================

PLAYER_WEAPON_MAP = {
    KNIGHT_ID: KNIGHT_WEAPON_ID,
    MONK_ID: MONK_WEAPON_ID,
    KILLER_ID: KILLER_WEAPON_ID,
    WIZARD_ID: WIZARD_WEAPON_ID,
    BOXER_ID: BOXER_WEAPON_ID,
    CAVEMAN_ID: CAVEMAN_WEAPON_ID,
}

# =========================
# SPEED
# =========================

KNIGHT_SPEED = 20
MONK_SPEED = 5
KILLER_SPEED = 5
WIZARD_SPEED = 5
BOXER_SPEED = 5
CAVEMAN_SPEED = 5

FIRST_ENEMY_SPEED = 0
SECOND_ENEMY_SPEED = 0
THIRD_ENEMY_SPEED = 0

FIRST_PROJECTILE_SPEED = 0
SECOND_PROJECTILE_SPEED = 0
THIRD_PROJECTILE_SPEED = 0

# =========================
# SPEED DATA
# =========================

SPEED_DATA = {
    PLAYER_ID: {
        KNIGHT_ID: KNIGHT_SPEED,
        MONK_ID: MONK_SPEED,
        KILLER_ID: KILLER_SPEED,
        WIZARD_ID: WIZARD_SPEED,
        BOXER_ID: BOXER_SPEED,
        CAVEMAN_ID: CAVEMAN_SPEED,
    },
    ENEMY_ID: {
        FIRST_ENEMY_ID: FIRST_ENEMY_SPEED,
        SECOND_ENEMY_ID: SECOND_ENEMY_SPEED,
        THIRD_ENEMY_ID: THIRD_ENEMY_SPEED,
    },
    PROJECTILE_ID: {
        FIRST_PROJECTILE_ID: FIRST_PROJECTILE_SPEED,
        SECOND_PROJECTILE_ID: SECOND_PROJECTILE_SPEED,
        THIRD_PROJECTILE_ID: THIRD_PROJECTILE_SPEED,
    },
}

# =========================
# MORE BUTTONS
# =========================

EXIT_BUTTON_ID = "B_E"
START_BUTTON_ID = "B_S"
KNIGHT_BUTTON_ID = "B_KN"
BOXER_BUTTON_ID = "B_BX"
WIZARD_BUTTON_ID = "B_WZ"
MONK_BUTTON_ID = "B_MK"
KILLER_BUTTON_ID = "B_KL"
CAVEMAN_BUTTON_ID = "B_CV"

START_BUTTON_TEXT = "Start"
EXIT_BUTTON_TEXT = "Exit"
KNIGHT_BUTTON_TEXT = "Knight"
BOXER_BUTTON_TEXT = "Boxer"
WIZARD_BUTTON_TEXT = "Wizard"
MONK_BUTTON_TEXT = "Monk"
KILLER_BUTTON_TEXT = "Killer"
CAVEMAN_BUTTON_TEXT = "Cave-\nman"

EXIT_BUTTON_WIDTH = 500
EXIT_BUTTON_HEIGHT = 200
START_BUTTON_WIDTH = 500
START_BUTTON_HEIGHT = 200
KNIGHT_BUTTON_WIDTH = 100
KNIGHT_BUTTON_HEIGHT = 400
BOXER_BUTTON_WIDTH = 100
BOXER_BUTTON_HEIGHT = 400
WIZARD_BUTTON_WIDTH = 100
WIZARD_BUTTON_HEIGHT = 400
MONK_BUTTON_WIDTH = 100
MONK_BUTTON_HEIGHT = 400
KILLER_BUTTON_WIDTH = 100
KILLER_BUTTON_HEIGHT = 400
CAVEMAN_BUTTON_WIDTH = 100
CAVEMAN_BUTTON_HEIGHT = 400

EXIT_BUTTON_POSITION = (150, 350)
START_BUTTON_POSITION = (150, 50)
KNIGHT_BUTTON_POSITION = (0, 100)
BOXER_BUTTON_POSITION = (140, 100)
WIZARD_BUTTON_POSITION = (280, 100)
MONK_BUTTON_POSITION = (420, 100)
KILLER_BUTTON_POSITION = (560, 100)
CAVEMAN_BUTTON_POSITION = (700, 100)

BUTTONS_DATA = {
    EXIT_BUTTON_ID: [EXIT_BUTTON_POSITION, EXIT_BUTTON_WIDTH, EXIT_BUTTON_HEIGHT],
    START_BUTTON_ID: [START_BUTTON_POSITION, START_BUTTON_WIDTH, START_BUTTON_HEIGHT],
    KNIGHT_BUTTON_ID: [KNIGHT_BUTTON_POSITION, KNIGHT_BUTTON_WIDTH, KNIGHT_BUTTON_HEIGHT],
    BOXER_BUTTON_ID: [BOXER_BUTTON_POSITION, BOXER_BUTTON_WIDTH, BOXER_BUTTON_HEIGHT],
    WIZARD_BUTTON_ID: [WIZARD_BUTTON_POSITION, WIZARD_BUTTON_WIDTH, WIZARD_BUTTON_HEIGHT],
    MONK_BUTTON_ID: [MONK_BUTTON_POSITION, MONK_BUTTON_WIDTH, MONK_BUTTON_HEIGHT],
    KILLER_BUTTON_ID: [KILLER_BUTTON_POSITION, KILLER_BUTTON_WIDTH, KILLER_BUTTON_HEIGHT],
    CAVEMAN_BUTTON_ID: [CAVEMAN_BUTTON_POSITION, CAVEMAN_BUTTON_WIDTH, CAVEMAN_BUTTON_HEIGHT],
}

# =========================
# BUTTON STYLE
# =========================

BUTTON_COLOR = (70, 70, 70)
BUTTON_BORDER_COLOR = (255, 255, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_BORDER_WIDTH = 2

BUTTON_FONT_NAME = "arial"
BUTTON_FONT_SIZE = 32

CHARACTER_SELECTION_ID = "CHARACTER_SELECTION"
PAUSED_TEXT = "PAUSED"

BUTTON_CHARACTER_MAP = {
    "knight_button": KNIGHT_ID,
    "boxer_button": BOXER_ID,
    "wizard_button": WIZARD_ID,
    "monk_button": MONK_ID,
    "killer_button": KILLER_ID,
    "caveman_button": CAVEMAN_ID,
}