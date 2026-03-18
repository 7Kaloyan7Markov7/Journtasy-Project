from scripts.entities.character import Character
from scripts.managers.asset_manager import AssetManager
from scripts.entities.weapon import Weapon
from scripts.collisions.hitbox import HitBox
import scripts.config.constants as const


class Player(Character):
    def __init__(self, entity_id, position, speed, level):
        super().__init__(entity_id, position, speed, level)
        self._experience = 0

        weapon_id = const.PLAYER_WEAPON_MAP[entity_id]
        self._weapon = Weapon(weapon_id, position, speed)
        self._sprites = AssetManager.get_player_animations(entity_id)

        hitbox_data = const.HITBOX_DATA[const.PLAYER_ID]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def weapon(self):
        return self._weapon

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def update(self):
        super().update()
        self.weapon.update()

    def render(self, screen):
        screen.blit(self.current_image, self.position)
        self.weapon.render(screen)

    def attack(self):
        pass

    def move(self):
        pass