from typing import Any

import numpy
from scipy.stats import skewnorm

from .PropertyGenerator import PropertyGenerator


class NormalNumberGenerator(PropertyGenerator):
    def __init__(self, mean: float, deviation: float, skew: float = 0, return_int: bool = False):
        """
        Init a NumberGenerator which will output number taken from a skewed normal distribution.

        :param skew: Skew parameters. Number below 0 will skew distribution to the left.
                    Set to 0 to have a standard Normal Number Generator.
        :param mean: Mean generated number
        :param deviation: deviation of the distribution
        :param return_int: return number as integer instead of float
        """
        self.skew = skew
        self.mean = mean
        self.deviation = deviation
        self.return_int = return_int

    def generate(self) -> Any:
        generated = skewnorm.rvs(self.skew, loc=self.mean, scale=self.deviation)
        if self.return_int:
            return numpy.asscalar(generated.round())
        else:
            return numpy.asscalar(generated)
