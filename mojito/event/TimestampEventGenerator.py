from typing import Any, Dict, List

from .EventGenerator import EventGenerator
from ..date.DateGenerator import DateGenerator
from ..property.PropertyGenerator import PropertyGenerator


class TimestampEventGenerator(EventGenerator):

    def __init__(self, timestamp: DateGenerator, properties: Dict[str, PropertyGenerator]):
        """
        Init an Event Generator based on a DateGenerator and multiples PropertyGenerator

        :param timestamp: a DateGenerator
        :param properties: a dict like {property_name: PropertyGenerator}
        """
        self.timestamp = timestamp
        self.properties = properties

    def generate(self) -> Dict[str, Any]:
        generated_properties = {name: prop.generate() for name, prop in self.properties.items()}
        return {
            "timestamp": self.timestamp.generate(),
            **generated_properties
            }

    def keys(self)-> List[str]:
        return [*list(self.properties.keys()), "timestamp"]
