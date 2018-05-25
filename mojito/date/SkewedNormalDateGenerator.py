from datetime import datetime

from scipy.stats import skewnorm

from .DateGenerator import DateGenerator


class SkewedNormalDateGenerator(DateGenerator):
    def __init__(self, loc: datetime, skew: float = 0, scale: float = 1):
        """
        Create a SkewedNormalDateGenerator. This generator is based on a second basis.

        It means that if you ask a date around 2018-01-01T00:00:00 with a scale of 10, you will get date +- 5s around
        this date.

        :param skew: Skew parameters. number below 0 will skew to the right, and above 0, to the left
        :param loc: Date around which we will generate date
        :param scale: scale, in second, for the range of random events
        """
        self.skew = skew
        self.loc = loc
        self.scale = scale

    def generate(self) -> datetime:
        timestamp = round(self.loc.timestamp())
        generated = skewnorm.rvs(self.skew, loc=timestamp, scale=self.scale)
        return datetime.fromtimestamp(generated)
