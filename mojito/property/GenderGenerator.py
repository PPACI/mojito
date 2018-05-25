from typing import Any

from numpy import random

from mojito.property.PropertyGenerator import PropertyGenerator


class GenderGenerator(PropertyGenerator):
    def __init__(self, women_probability: float = 0.5):
        self.women_probability = women_probability

    def generate(self) -> Any:
        if random.random() < self.women_probability:
            return "F"
        else:
            return "M"
