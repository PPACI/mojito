from typing import Any, Dict

from mojito.property.PropertyGenerator import PropertyGenerator
from .date.DateGenerator import DateGenerator


class Event:
    def __init__(self, date: DateGenerator, properties: Dict[str, PropertyGenerator]):
        self.date = date
        self.properties = properties

    def generate(self) -> Dict[str, Any]:
        generated_properties = {name: prop.generate() for name, prop in self.properties.items()}
        return {
            "timestamp": self.date.generate(),
            **generated_properties
            }
