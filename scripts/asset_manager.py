import pygame
import constants as const
from enums import Direction

class AssetManager:
    
    @classmethod
    def get_image(cls, frames, frame_index, frame_width, frame_height, scale, color):
        canvas = pygame.Surface((frame_width,frame_height)).convert_alpha() #creates a surface to draw on
        canvas.blit(frames, const.TOP_LEFT_CORNER , (frame_index * (frame_width + 14), 0, frame_width, frame_height)) #crops the n-th frame from the sprite sheet
        image = pygame.transform.scale(canvas, (frame_width * scale, frame_height * scale)) #makes additional sprite transformation
        image.set_colorkey(color) #makes the background transparent, so only the sprite is left
 
        return image
    
    @classmethod
    def load_animations(cls, entity_id):
        if "!" in entity_id: #every playable character will have ! in their ID
            return cls.load_player_animations(entity_id)
        elif "@" in entity_id:
            return cls.load_projectile_animations(entity_id)

    @classmethod
    def get_all_frames(cls, file_path, width, height, scale):
        frames = pygame.image.load(file_path).convert_alpha()
        all_sprites = []

        for i in range(0,5):
            all_sprites.append(cls.get_image(frames, i, width, height, scale, (0,0,0)))
    
        return all_sprites
    
    @classmethod
    def load_player_animations(cls, entity_id):
        animations = {}

        sprite_file_paths = const.PLAYER_SPRITE_FILES[entity_id]

        animations[Direction.DOWN] = cls.get_all_frames(sprite_file_paths[0], 31, 31, 3)
        animations[Direction.UP] = cls.get_all_frames(sprite_file_paths[1], 31, 31, 3)
        animations[Direction.LEFT] = cls.get_all_frames(sprite_file_paths[2], 31, 31, 3)
        animations[Direction.RIGHT] = cls.get_all_frames(sprite_file_paths[3], 31, 31, 3)

        return animations

    
    def load_projectile_animations(entity_id):
        ...

    @classmethod
    def load_all():
        ...