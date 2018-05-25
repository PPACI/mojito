from abc import ABC, abstractmethod
from typing import Dict, Any


class EventGenerator(ABC):
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        raise NotImplementedError
