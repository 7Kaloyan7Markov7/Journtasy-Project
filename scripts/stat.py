from abc import ABC, abstractmethod


class Stat(ABC):

    @abstractmethod
    def increase(self):
        raise NotImplementedError