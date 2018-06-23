from typing import Any

import numpy
from scipy.stats import poisson

from .PropertyGenerator import PropertyGenerator


class PoissonNumberGenerator(PropertyGenerator):
    def __init__(self, mu: float, return_int: bool = False):
        """
        Init a NumberGenerator which will output number taken from a skewed normal distribution.

        :param mu: average number of events per interval.
        :param return_int: return number as integer instead of float
        """
        self.mu = mu
        self.return_int = return_int

    def generate(self) -> Any:
        generated = poisson.rvs(self.mu)
        if self.return_int:
            return numpy.asscalar(generated.round())
        else:
            return numpy.asscalar(generated)
