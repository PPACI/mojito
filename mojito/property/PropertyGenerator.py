from abc import ABC, abstractmethod
from typing import Any


class PropertyGenerator(ABC):
    @abstractmethod
    def generate(self) -> Any:
        """
        Generate a random property

        :return: a random property
        """
        raise NotImplementedError
