from abc import ABC, abstractmethod


class Scene(ABC):
    scene_id = None
    
    @abstractmethod
    def render(self, screen):
        raise NotImplementedError