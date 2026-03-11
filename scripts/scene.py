class Scene:
    def __init__(self, room):
        self.room = room

    def update(self):
        self.room.update()

    def render(self):
        self.room.render()