from scripts.entities.character import Character
from scripts.gui.health_bar_ui import HealthBarUI


class GUI:
    def __init__(self):
        self._health_bar = HealthBarUI()

    def _get_entities(self, room):
        entities = []
        if room.player is not None:
            entities.append(room.player)
        for entity in room.entity_list:
            if isinstance(entity, Character) and entity not in entities:
                entities.append(entity)
        return entities

    def render(self, screen, room):
        for entity in self._get_entities(room):
            self._health_bar.update(entity)
            self._health_bar.render(screen)