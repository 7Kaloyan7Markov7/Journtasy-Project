from scene import Scene
import constants as const


class GameScene(Scene):
    scene_id = const.GAME_SCENE_ID

    def __init__(self, room):
        self.room = room
        self.is_paused = False

    def update(self):
        if not self.is_paused:
            self.room.update()

    def render(self, screen):
        self.room.render(screen)

    def pause(self):
        self.is_paused = not self.is_paused