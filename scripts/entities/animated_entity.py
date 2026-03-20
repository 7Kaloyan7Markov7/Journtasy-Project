from scripts.entities.entity import Entity


class AnimatedEntity(Entity):
    def __init__(self, entity_id, position, speed):
        super().__init__(entity_id, position, speed)
        self._current_frame_index = 0
        self._sprites = {}

    @property
    def current_frame_index(self):
        return self._current_frame_index

    def animate(self, frames):
        if not frames:
            return

        self._current_frame_index += 1

        if self._current_frame_index >= len(frames):
            self._current_frame_index = 0

    def reset_animation(self):
        self._current_frame_index = 0