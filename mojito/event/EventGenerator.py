from abc import ABC, abstractmethod
from typing import Any, Dict, List


class EventGenerator(ABC):
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def keys(self) -> List[str]:
        raise NotImplementedError
