import pygame 
import constants as const


import pygame


class InputManager:
    def __init__(self):
        self._move_up = False
        self._move_down = False
        self._move_left = False
        self._move_right = False

        self._attack_pressed = False
        self._pause_pressed = False
        self._quit_pressed = False

        self._left_click_position = None
        self._right_click_position = None

    @property
    def move_up(self):
        return self._move_up

    @property
    def move_down(self):
        return self._move_down

    @property
    def move_left(self):
        return self._move_left

    @property
    def move_right(self):
        return self._move_right

    @property
    def attack_pressed(self):
        return self._attack_pressed

    @property
    def pause_pressed(self):
        return self._pause_pressed

    @property
    def quit_pressed(self):
        return self._quit_pressed

    @property
    def left_click_position(self):
        return self._left_click_position

    @property
    def right_click_position(self):
        return self._right_click_position

    def update(self):
        self._move_up = False
        self._move_down = False
        self._move_left = False
        self._move_right = False

        self._attack_pressed = False
        self._pause_pressed = False
        self._quit_pressed = False

        self._left_click_position = None
        self._right_click_position = None

        keys = pygame.key.get_pressed()
        self._move_up = keys[pygame.K_w]
        self._move_down = keys[pygame.K_s]
        self._move_left = keys[pygame.K_a]
        self._move_right = keys[pygame.K_d]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_pressed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._pause_pressed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self._attack_pressed = True
                    self._left_click_position = event.pos

                if event.button == pygame.BUTTON_RIGHT:
                    self._right_click_position = event.pos