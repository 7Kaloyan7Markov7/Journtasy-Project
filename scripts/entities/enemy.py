from random import choice

from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction
import scripts.config.constants as const


class Enemy(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)

        self._sprites = AssetManager.get_enemy_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.ENEMY_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])
        
        self._exp_base = const.ENEMY_EXP_DROPS[entity_id][0]
        self._exp_growth = const.ENEMY_EXP_DROPS[entity_id][1]

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]
    
    @property
    def exp_on_kill(self):
        return self._exp_base + self.stats.level * self._exp_base * self._exp_base

    def update(self):
        if self.stats.is_dead: return 

        super().update()
        self.move()
        self.animate()

    def render(self, screen):
        if self.stats.is_dead: return 
        
        screen.blit(self.current_image, self.position)

    def attack(self, target):
        pass

    def move(self):
        directions = [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]
        random_direction = choice(directions)

        self._direction = random_direction

        if random_direction == Direction.DOWN:
            self.position.y += self.speed
        
        if random_direction == Direction.UP:
            self.position.y -= self.speed
        
        if random_direction == Direction.RIGHT:
            self.position.x += self.speed

        if random_direction == Direction.LEFT:
            self.position.x -= self.speed
