from typing import Any

from .PropertyGenerator import PropertyGenerator


class FixedValueGenerator(PropertyGenerator):
    def __init__(self, value: Any):
        self.value = value

    def generate(self) -> Any:
        return self.value
