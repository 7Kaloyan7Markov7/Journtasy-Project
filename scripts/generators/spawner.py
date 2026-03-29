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
        return PlayerGenerator(choice).generate()

    def spawn_enemy(self):
        return self._enemy_generator.generate()

    def spawn_obstacle(self):
        return self._obstacle_generator.generate()

    def _is_position_free(self, entity, existing_entities):
        return all(
            not entity.hitbox.is_colliding(existing.hitbox)
            for existing in existing_entities
        )

    def _reposition(self, entity):
        new_x = randint(200 + entity.width, const.SCREEN_WIDTH - entity.width - 200)
        new_y = randint(200 + entity.height, const.SCREEN_HEIGHT - entity.height - 200)
        new_pos = Vector2(new_x, new_y)
        entity.position = new_pos
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

        for _ in range(randint(1, 5)):
            enemy = self._spawn_without_overlap(self.spawn_enemy, entity_list)
            if enemy is not None:
                entity_list.append(enemy)

        for _ in range(randint(1, 3)):
            obstacle = self._spawn_without_overlap(self.spawn_obstacle, entity_list)
            if obstacle is not None:
                entity_list.append(obstacle)

        return entity_list
