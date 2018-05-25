# Mojito


Mocking temporal data made easy !

## Example
```python
from datetime import datetime

from mojito.date.SkewedNormalDateGenerator import SkewedNormalDateGenerator
from mojito.event.TimestampEventGenerator import TimestampEventGenerator
from mojito.property.RandomChoiceGenerator import RandomChoiceGenerator
from mojito.property.SkewedNormalNumberGenerator import SkewedNormalNumberGenerator

generator = TimestampEventGenerator(timestamp=SkewedNormalDateGenerator(loc=datetime.now(), scale=3600, skew=-5),
                                    properties={
                                        "gender": RandomChoiceGenerator(['M', 'F'], weights=[1, 10]),
                                        "age": SkewedNormalNumberGenerator(loc=18, scale=4, return_int=True)
                                        })
for _ in range(10):
    print(generator.generate())
print("#####")
```