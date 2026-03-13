class Room:
    def __init__(self, background, entity_list):
        self.background = background
        self.entity_list = entity_list

    def render(self, screen):
        self.background.render(screen)

        for entity in self.entity_list:
            entity.render(screen)

    def update(self):
        for entity in self.entity_list:
            entity.update()