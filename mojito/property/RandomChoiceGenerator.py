import random
from typing import Any, List, Optional

import numpy

from .PropertyGenerator import PropertyGenerator


class RandomChoiceGenerator(PropertyGenerator):
    def __init__(self, initial_list: List[Any], weights: Optional[List[float]]):
        self.initial_list = initial_list
        if weights is not None:
            assert len(weights) == len(initial_list), "Len of weights and initial_list should be the same"
        else:
            weights = numpy.ones(len(initial_list))
        self.weights = weights

    def generate(self) -> Any:
        choices = random.choices(self.initial_list, weights=self.weights)
        return choices[0]
