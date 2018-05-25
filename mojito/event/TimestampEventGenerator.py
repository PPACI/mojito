from typing import Any, Dict

from .EventGenerator import EventGenerator
from ..property.PropertyGenerator import PropertyGenerator
from ..date.DateGenerator import DateGenerator


class TimestampEventGenerator(EventGenerator):
    def __init__(self, timestamp: DateGenerator, properties: Dict[str, PropertyGenerator]):
        self.timestamp = timestamp
        self.properties = properties

    def generate(self) -> Dict[str, Any]:
        generated_properties = {name: prop.generate() for name, prop in self.properties.items()}
        return {
            "timestamp": self.timestamp.generate(),
            **generated_properties
            }
