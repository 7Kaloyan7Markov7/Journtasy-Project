import pygame 
import constants as const


MOVE_UP_KEY = pygame.K_w
MOVE_DOWN_KEY = pygame.K_s
MOVE_LEFT_KEY = pygame.K_a
MOVE_RIGHT_KEY = pygame.K_d
PAUSE_KEY = pygame.K_ESCAPE

class InputManager:
    def __init__(self):
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.attack_pressed = False
        self.pause_pressed = False
        self.quit_pressed = False

        self.left_click_position = None
        self.right_click_position = None

    def update(self):
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        self.attack_pressed = False
        self.pause_pressed = False
        self.quit_pressed = False

        self.left_click_position = None
        self.right_click_position = None

        keys = pygame.key.get_pressed()
        self.move_down = keys[pygame.K_w]
        self.move_down = keys[pygame.K_s]
        self.move_left = keys[pygame.K_a]
        self.move_right = keys[pygame.K_d]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_requested = True

        if event.type == pygame.KEYDOWN:
            if event.key == const.PAUSE_KEY:
                self.pause_pressed = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT: #left click
                self.attack_pressed = True
                self.left_click_position = event.pos
            if event.button == pygame.BUTTON_RIGHT: #right click
                self.right_click_position = event.pos