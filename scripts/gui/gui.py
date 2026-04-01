from scripts.entities.character import Character


class GUI:
    def __init__(self):
        self._health_bar = 0

    def render(self, screen, room):
        entities_to_draw = []

        if room.player is not None:
            entities_to_draw.append(room.player)

        for entity in room.entity_list:
            if isinstance(entity, Character) and entity not in entities_to_draw:
                entities_to_draw.append(entity)

        for entity in entities_to_draw:
            if entity.stats.is_dead:
                continue
            self._health_bar.render(screen, entity)