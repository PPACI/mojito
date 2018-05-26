from datetime import datetime

from scipy.stats import skewnorm

from .DateGenerator import DateGenerator


class SkewedNormalDateGenerator(DateGenerator):
    def __init__(self, center: datetime, skew: float = 0, deviation: float = 1):
        """
        Create a SkewedNormalDateGenerator. This generator is based on a second basis.

        It means that if you ask a date around 2018-01-01T00:00:00 with a scale of 10, you will get date +- 5s around
        this date.

        :param skew: Skew parameters. Number below 0 will result in more date to the left limit.
        :param center: Mean generated datetime for the skewed normal distribution
        :param deviation: Deviation of datetime, in second, used for the skewed normal distribution
        """
        self.skew = skew
        self.center = center
        self.dispersion = deviation

    def generate(self) -> datetime:
        """
        Generate a random date taken from a Skewed Normal Distribution

        :return: datetime
        """
        timestamp = round(self.center.timestamp())
        generated = skewnorm.rvs(self.skew, loc=timestamp, scale=self.dispersion)
        return datetime.fromtimestamp(generated)
