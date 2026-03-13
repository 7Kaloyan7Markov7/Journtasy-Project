from abc import ABC, abstractmethod


class Scene(ABC):
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def render(self, screen):
        pass