from typing import Any, Dict, List

from .EventGenerator import EventGenerator
from ..property.PropertyGenerator import PropertyGenerator


class PropertyEventGenerator(EventGenerator):

    def __init__(self, properties: Dict[str, PropertyGenerator]):
        """
        Init an Event Generator based on a DateGenerator and multiples PropertyGenerator

        :param properties: a dict like {property_name: PropertyGenerator}
        """
        self.properties = properties

    def generate(self) -> Dict[str, Any]:
        generated_properties = {name: prop.generate() for name, prop in self.properties.items()}
        return {
            **generated_properties
            }

    def keys(self)-> List[str]:
        return [*list(self.properties.keys())]
