import pygame
import constants as const
from enums import Direction


class AssetManager:
    @staticmethod
    def crop_sprite(frames, frame_index, frame_width, frame_height, scale, frame_space):
        canvas = pygame.Surface((frame_width,frame_height)).convert_alpha() #creates a surface to draw on
        canvas.blit(frames, const.TOP_LEFT_CORNER , (frame_index * (frame_width + frame_space), 0, frame_width, frame_height)) #crops the n-th frame from the sprite sheet
        image = pygame.transform.scale(canvas, (frame_width * scale, frame_height * scale)) #makes additional sprite transformation
       #image.set_colorkey(color)
       # #makes the background transparent, so only the sprite is left

        return image
    
    @staticmethod
    def load_animations(entity_id):
        if const.PLAYER_ID_SYMB in entity_id: #every playable character will have "!" in their ID
            return AssetManager.load_player_animations(entity_id)
        
        elif const.PROJECTILE_ID_SYMB in entity_id: #every projectile will have "@" in their ID
            return AssetManager.load_projectile_animations(entity_id)
        
        elif const.ENEMY_ID_SYMB in entity_id: #every enemy will have "#" in their ID
            return AssetManager.load_enemy_animations(entity_id)
        
        #every obstacle will have "&" in their ID
        return AssetManager.load_obstacle_animations(entity_id)
        
    @staticmethod
    def get_all_frames(file_path, frame_width, frame_height, scale, frame_count, frame_space):
        frames = pygame.image.load(file_path).convert_alpha()
        direction_sprites = []

        for i in range(0, frame_count):
            direction_sprites.append(AssetManager.crop_sprite(frames, i, frame_width, frame_height, scale , frame_space))
    
        return direction_sprites

    #load entity animations and sprites
    @staticmethod
    def load_player_animations(entity_id):
        animations = {}

        sprite_file_paths = const.PLAYER_SPRITE_FILES[entity_id]

        animations[Direction.DOWN] = AssetManager.get_all_frames(sprite_file_paths[0], const.PLAYER_SPRITE_WIDTH, const.PLAYER_SPRITE_HEIGHT, 3, const.PLAYER_FRAME_COUNT, const.PLAYER_FRAME_SPACE)
        animations[Direction.UP] = AssetManager.get_all_frames(sprite_file_paths[1], const.PLAYER_SPRITE_WIDTH, const.PLAYER_SPRITE_HEIGHT, 3, const.PLAYER_FRAME_COUNT, const.PLAYER_FRAME_SPACE)
        animations[Direction.LEFT] = AssetManager.get_all_frames(sprite_file_paths[2], const.PLAYER_SPRITE_WIDTH, const.PLAYER_SPRITE_HEIGHT, 3, const.PLAYER_FRAME_COUNT, const.PLAYER_FRAME_SPACE)
        animations[Direction.RIGHT] = AssetManager.get_all_frames(sprite_file_paths[3], const.PLAYER_SPRITE_WIDTH, const.PLAYER_SPRITE_HEIGHT, 3, const.PLAYER_FRAME_COUNT, const.PLAYER_FRAME_SPACE)

        return animations

    @staticmethod
    def load_projectile_animations(entity_id):
        ...

    @staticmethod
    def load_enemy_animations(entity_id):
        ...

    @staticmethod
    def load_obstacle_animations(entity_id):
        ...

    def load_static_images():
        ...

    @staticmethod
    def load_assets(entity_list):
        for entity in entity_list:
            entity.load()