from scene import Scene


class GameScene(Scene):
    def __init__(self, room):
        self.room = room
        self.is_paused = False

    def update(self):
        self.room.update()

    def render(self, screen):
        self.room.render(screen)

    def pause_unpause(self):
        self.is_paused = not self.is_paused