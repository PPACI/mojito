from abc import ABC, abstractmethod
from typing import Any


class PropertyGenerator(ABC):
    @abstractmethod
    def generate(self) -> Any:
        raise NotImplementedError
