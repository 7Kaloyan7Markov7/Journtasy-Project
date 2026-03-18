from abc import ABC, abstractmethod


class Generator(ABC):

    @abstractmethod
    def generate(self):
        raise NotImplementedError