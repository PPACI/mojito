from abc import ABC, abstractmethod
from typing import Any, Dict, List


class EventGenerator(ABC):
    @abstractmethod
    def generate(self) -> Dict[str, Any]:
        """
        Generate a random event

        :return: a dict like {property_name: value}
        """
        raise NotImplementedError

    @abstractmethod
    def keys(self) -> List[str]:
        """
        Return the list of properties name contained in this event generator

        :return: a list of properties name
        """
        raise NotImplementedError
