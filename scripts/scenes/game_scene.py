from scripts.scenes.scene import Scene
import scripts.config.constants as const


class GameScene(Scene):
    scene_id = const.GAME_SCENE_ID

    def __init__(self, room):
        self._room = room
        self._is_paused = False

    @property
    def room(self):
        return self._room
    
    @property
    def is_paused(self):
        return self._is_paused
    
    @room.setter
    def room(self, new_room):
        self._room = new_room

    def update(self):
        if not self.is_paused:
            self._room.update()

    def render(self, screen):
        self._room.render(screen)

    def pause(self):
        self._is_paused = not self._is_paused