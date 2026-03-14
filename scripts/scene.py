from abc import ABC, abstractmethod


class Scene(ABC):
    scene_id = None

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def render(self, screen):
        pass