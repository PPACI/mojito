from typing import Any

from .PropertyGenerator import PropertyGenerator


class FixedValueGenerator(PropertyGenerator):
    def __init__(self, value: Any):
        """
        Init a FixedValueGenerator which will always generate the same value. Used for non-changing property.

        :param value: value to output
        """
        self.value = value

    def generate(self) -> Any:
        return self.value
