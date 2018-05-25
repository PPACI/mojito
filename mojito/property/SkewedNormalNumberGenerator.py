from typing import Any

import numpy
from scipy.stats import skewnorm

from .PropertyGenerator import PropertyGenerator


class SkewedNormalNumberGenerator(PropertyGenerator):
    def __init__(self, loc: float, scale: float, skew: float = 0, return_int: bool = False):
        """
        Create a SkewedNormalNumberGenerator.

        :param skew: Skew parameters. Number below 0 will result in more date to the left limit.
                    Set to 0 to have a standard Normal Number Generator.
        :param loc: Mean generated number
        :param scale: dispersion of the distribution
        """
        self.skew = skew
        self.loc = loc
        self.scale = scale
        self.return_int = return_int

    def generate(self) -> Any:
        generated = skewnorm.rvs(self.skew, loc=self.loc, scale=self.scale)
        if self.return_int:
            return numpy.asscalar(generated.round())
        else:
            return numpy.asscalar(generated)
