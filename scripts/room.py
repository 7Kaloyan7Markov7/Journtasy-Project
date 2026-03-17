class Room:
    def __init__(self, background, entity_list):
        self._background = background
        self._entity_list = entity_list

    @property
    def entity_list(self):
        return self._entity_list

    def render(self, screen):
        self._background.render(screen)

        for entity in self.entity_list:
            entity.render(screen)

    def update(self):
        for entity in self.entity_list:
            entity.update()