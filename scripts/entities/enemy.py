from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.collisions.hitbox import HitBox
from scripts.enums.enums import Direction, State
import scripts.config.constants as const
import pygame


class Enemy(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)

        self._sprites = AssetManager.get_enemy_animations(entity_id)
        self._attack_sprites = AssetManager.get_enemy_attack_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.ENEMY_ID][entity_id]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

        self._attack_cooldown = 0
        self._attack_delay = const.ENEMY_ATTACK_DELAY
        self._is_attacking = False
        self._attack_frame_index = 0

        self._is_aggroed = False
        self._aggro_box = HitBox(self._hitbox.hitbox.center, const.ENEMY_AGGRO_SIZE, const.ENEMY_AGGRO_SIZE, True)

        self._exp_base = const.ENEMY_EXP_DROPS[entity_id][0]
        self._exp_growth = const.ENEMY_EXP_DROPS[entity_id][1]

    @property
    def is_aggroed(self):
        return self._is_aggroed
    
    @is_aggroed.setter
    def is_aggroed(self, value):
        self._is_aggroed = value

    @property
    def aggro_box(self):
        return self._aggro_box

    @property
    def current_image(self):
        if self._is_attacking:
            return self._attack_sprites[self.direction][self._attack_frame_index]
        return self._sprites[self.direction][self.current_frame_index]
    
    @property
    def exp_on_kill(self):
        return self._exp_base + self.stats.level * self._exp_growth * self._exp_base

    def update(self):
        if self.stats.is_dead:
            return

        super().update()
        self.hitbox.move(self.position)
        self._update_aggro_box()

        if self._attack_cooldown > 0:
            self._attack_cooldown -= 1

        if self._is_attacking:
            self.animate_attack()
        elif self.state != State.IDLE:
            self.animate()

    def render(self, screen):
        if self.stats.is_dead: return 
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox.hitbox)
        pygame.draw.rect(screen, (255, 0, 0), self.aggro_box.hitbox, 2)
        screen.blit(self.current_image, self.position)

    def animate_attack(self):
        frame_count = len(self._attack_sprites[self.direction])
        self._attack_frame_index += 1
        if self._attack_frame_index >= frame_count:
            self._attack_frame_index = 0
            self._is_attacking = False

    def attack(self, target):
        if self._attack_cooldown > 0:
            return

        target.take_damage(self.stats.damage.damage)
        self._attack_cooldown = self._attack_delay
        self._is_attacking = True
        self._attack_frame_index = 0

    def _update_aggro_box(self):
        self._aggro_box.move(self._hitbox.hitbox.center)

    def move(self, player):
        dx = player.position.x - self.position.x
        dy = player.position.y - self.position.y

        distance = (dx ** 2 + dy ** 2) ** 0.5
        if distance == 0 or self._hitbox.is_colliding(player.hitbox):
            return  
        
        self.state = State.MOVING
        
        if abs(dx) > abs(dy):
            if dx > 0:
                self._direction = Direction.RIGHT
            else:
                self._direction = Direction.LEFT
        else:
            if dy > 0:
                self._direction = Direction.DOWN
            else:
                self._direction = Direction.UP

        self.previous_position.x = self.position.x
        self.previous_position.y = self.position.y

        self.position.x += (dx / distance) * self.speed
        self.position.y += (dy / distance) * self.speed
