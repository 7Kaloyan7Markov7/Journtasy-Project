from random import randint
from pygame import Vector2

from scripts.generators.enemy_generator import EnemyGenerator
from scripts.generators.player_generator import PlayerGenerator
from scripts.generators.obstacle_generator import ObstacleGenerator
import scripts.config.constants as const


class Spawner:
    def __init__(self):
        self._enemy_generator = EnemyGenerator()
        self._obstacle_generator = ObstacleGenerator()

    def spawn_player(self, choice):
        player_generator = PlayerGenerator(choice)
        return player_generator.generate()

    def spawn_enemy(self):
        return self._enemy_generator.generate()

    def spawn_obstacle(self):
        return self._obstacle_generator.generate()

    def _is_position_free(self, entity, existing_entities):
        for existing in existing_entities:
            if entity.hitbox.is_colliding(existing.hitbox):
                return False
        return True

    def _reposition(self, entity):
        new_x = randint(200 + entity.width, const.SCREEN_WIDTH - entity.width - 200)
        new_y = randint(200 + entity.height, const.SCREEN_HEIGHT - entity.height - 200)
        new_pos = Vector2(new_x, new_y)
        entity.position = entity._position.__class__(new_pos) 
        entity.hitbox.move(new_pos)

    def _spawn_without_overlap(self, spawn_fn, existing_entities, max_attempts=100):
        entity = spawn_fn()
        for _ in range(max_attempts):
            if self._is_position_free(entity, existing_entities):
                return entity
            self._reposition(entity)
        return None

    def spawn_entities(self):
        entity_list = []

        count_of_enemies = randint(1, 5)
        for _ in range(count_of_enemies):
            enemy = self._spawn_without_overlap(self.spawn_enemy, entity_list)
            if enemy is not None:
                entity_list.append(enemy)

        count_of_obstacles = randint(1, 3)
        for _ in range(count_of_obstacles):
            obstacle = self._spawn_without_overlap(self.spawn_obstacle, entity_list)
            if obstacle is not None:
                entity_list.append(obstacle)

        return entity_list