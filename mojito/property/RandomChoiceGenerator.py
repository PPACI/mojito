import random
from typing import Any, List, Optional

import numpy

from .PropertyGenerator import PropertyGenerator


class RandomChoiceGenerator(PropertyGenerator):
    def __init__(self, initial_list: List[Any], weights: Optional[List[float]] = None):
        """
        Init a RandomChoiceGenerator which will output a random choice in the given list.

        :param initial_list: list to randomly take value
        :param weights: Optional weights list used to alter the probabilities
        """
        self.initial_list = initial_list
        if weights is not None:
            assert len(weights) == len(initial_list), "Len of weights and initial_list should be the same"
        else:
            weights = numpy.ones(len(initial_list))
        self.weights = weights

    def generate(self) -> Any:
        choices = random.choices(self.initial_list, weights=self.weights)
        return choices[0]
