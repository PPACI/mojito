from abc import ABC, abstractmethod
from datetime import datetime


class DateGenerator(ABC):
    @abstractmethod
    def generate(self) -> datetime:
        raise NotImplementedError
