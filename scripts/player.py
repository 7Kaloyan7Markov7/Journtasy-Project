from character import Character
from asset_manager import AssetManager
from weapon import Weapon
from hitbox import HitBox
import constants as const


class Player(Character):
    def __init__(self, player_id, position, speed, stats):
        super().__init__(player_id, position, speed, stats)
        self._experience = 0

        weapon_id = const.PLAYER_WEAPON_MAP[player_id]
        self._weapon = Weapon(weapon_id, position, speed)
        self._sprites = AssetManager.get_player_animations(player_id)

        hitbox_data = const.HITBOX_DATA[const.PLAYER_ID]
        self._hitbox = HitBox(position, hitbox_data[0], hitbox_data[1])

    @property
    def weapon(self):
        return self._weapon

    @property
    def hitbox(self):
        return self._hitbox

    @property
    def current_image(self):
        return self._sprites[self.direction][self.current_frame_index]

    def update(self):
        self.weapon.update()

    def render(self, screen):
        screen.blit(self.current_image, self.position)
        self.weapon.render(screen)

    def attack(self):
        pass

    def move(self):
        pass