import pygame
import constants as const
from enums import Direction


class AssetManager:
    backgrounds = {}
    obstacle_images = {}
    player_animations = {}
    projectile_animations = {}
    enemy_animations = {}
    weapon_animations = {}

    @staticmethod
    def crop_sprite(frames, frame_index, frame_width, frame_height, scale, frame_space):
        canvas = pygame.Surface((frame_width,frame_height)).convert_alpha() #creates a surface to draw on
        canvas.blit(frames, const.TOP_LEFT_CORNER , (frame_index * (frame_width + frame_space), 0, frame_width, frame_height)) #crops the n-th frame from the sprite sheet
        image = pygame.transform.scale(canvas, (frame_width * scale, frame_height * scale)) #makes additional sprite transformation
       #image.set_colorkey(color)
       # #makes the background transparent, so only the sprite is left

        return image
    
    @staticmethod
    def get_all_frames(file_path, frame_width, frame_height, scale, frame_count, frame_space):
        frames = pygame.image.load(file_path).convert_alpha()
        direction_sprites = []

        for i in range(0, frame_count):
            direction_sprites.append(AssetManager.crop_sprite(frames, i, frame_width, frame_height, scale , frame_space))
    
        return direction_sprites

    @staticmethod
    def load_image(file_path, scale=1):
        image = pygame.image.load(file_path).convert_alpha()

        if scale != 1:
            image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

        return image

    @staticmethod
    def load_four_direction_animations(entity_id, sprite_file_dict, frame_width, frame_height, scale, frame_count, frame_space):
        animations = {}
        sprite_file_paths = sprite_file_dict[entity_id]

        animations[Direction.DOWN] = AssetManager.get_all_frames(sprite_file_paths[0], frame_width, frame_height, scale, frame_count, frame_space)
        animations[Direction.UP] = AssetManager.get_all_frames(sprite_file_paths[1], frame_width, frame_height, scale, frame_count, frame_space)
        animations[Direction.LEFT] = AssetManager.get_all_frames(sprite_file_paths[2], frame_width, frame_height, scale, frame_count, frame_space)
        animations[Direction.RIGHT] = AssetManager.get_all_frames(sprite_file_paths[3], frame_width, frame_height, scale, frame_count, frame_space)

        return animations

    @staticmethod
    def load_two_direction_animations(entity_id, sprite_file_dict, frame_width, frame_height, scale, frame_count, frame_space):
        animations = {}
        sprite_file_paths = sprite_file_dict[entity_id]

        animations[Direction.LEFT] = AssetManager.get_all_frames(sprite_file_paths[0], frame_width, frame_height, scale, frame_count, frame_space)
        animations[Direction.RIGHT] = AssetManager.get_all_frames(sprite_file_paths[1], frame_width, frame_height, scale, frame_count, frame_space)

        return animations

    @staticmethod
    def load_player_animations(entity_id):
        return AssetManager.load_four_direction_animations(
            entity_id,
            const.PLAYER_SPRITE_FILES,
            const.PLAYER_SPRITE_WIDTH,
            const.PLAYER_SPRITE_HEIGHT,
            const.PLAYER_SCALE,
            const.PLAYER_FRAME_COUNT,
            const.PLAYER_FRAME_SPACE
        )

    @staticmethod
    def load_projectile_animations(entity_id):
        return AssetManager.load_four_direction_animations(
            entity_id,
            const.PROJECTILE_SPRITE_FILES,
            const.PROJECTILE_WIDTH,
            const.PROJECTILE_HEIGHT,
            const.PROJECTILE_SCALE,
            const.PROJECTILE_FRAME_COUNT,
            const.PROJECTILE_FRAME_SPACE
        )

    @staticmethod
    def load_enemy_animations(entity_id):
        return AssetManager.load_four_direction_animations(
            entity_id,
            const.ENEMY_SPRITE_FILES,
            const.ENEMY_WIDTH,
            const.ENEMY_HEIGHT,
            const.ENEMY_SCALE,
            const.ENEMY_FRAME_COUNT,
            const.ENEMY_FRAME_SPACE
        )

    @staticmethod
    def load_weapon_animations(entity_id):
        return AssetManager.load_two_direction_animations(
            entity_id,
            const.WEAPON_SPRITE_FILES,
            const.WEAPON_WIDTH,
            const.WEAPON_HEIGHT,
            const.WEAPON_SCALE,
            const.WEAPON_FRAME_COUNT,
            const.WEAPON_FRAME_SPACE
        )

    @staticmethod
    def load_backgrounds():
        for background_id, path in const.BACKGROUND_PATHS.items():
            AssetManager.backgrounds[background_id] = AssetManager.load_image(path, scale=const.BACKGROUND_SCALE, alpha=False)

    @staticmethod
    def load_obstacle_images():
        for obstacle_id, path in const.OBSTACLE_IMAGE_FILES.items():
            AssetManager.obstacle_images[obstacle_id] = AssetManager.load_image(path, scale=const.OBSTACLE_SCALE, alpha=True)

    @staticmethod
    def load():
        for player_id in const.PLAYABLE_CHARACTER_IDS:
            AssetManager.player_animations[player_id] = AssetManager.load_player_animations(player_id)

        for projectile_id in const.PROJECTILE_IDS:
            AssetManager.projectile_animations[projectile_id] = AssetManager.load_projectile_animations(projectile_id)

        for enemy_id in const.ENEMY_IDS:
            AssetManager.enemy_animations[enemy_id] = AssetManager.load_enemy_animations(enemy_id)

        for weapon_id in const.WEAPON_IDS:
            AssetManager.weapon_animations[weapon_id] = AssetManager.load_weapon_animations(weapon_id)

        AssetManager.load_backgrounds()
        AssetManager.load_obstacle_images()


    #getters
    @staticmethod
    def get_background(background_id):
        return AssetManager.backgrounds[background_id]

    @staticmethod
    def get_obstacle_image(obstacle_id):
        return AssetManager.obstacle_images[obstacle_id]

    @staticmethod
    def get_player_animations(player_id):
        return AssetManager.player_animations[player_id]

    @staticmethod
    def get_projectile_animations(projectile_id):
        return AssetManager.projectile_animations[projectile_id]

    @staticmethod
    def get_enemy_animations(enemy_id):
        return AssetManager.enemy_animations[enemy_id]

    @staticmethod
    def get_weapon_animations(weapon_id):
        return AssetManager.weapon_animations[weapon_id]