from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply(self, order):
        pass
