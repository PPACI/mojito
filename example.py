from datetime import datetime
from pprint import pprint

from mojito import (
    DateGenerator,
    EventComposer,
    NumberGenerator,
    PropertyEventGenerator,
    RandomChoiceGenerator,
)

first = PropertyEventGenerator(
    properties={
        "timestamp": DateGenerator(
            center=datetime(2018, 1, 1, 13, 0, 0), deviation=3600
        ),
        "age": NumberGenerator(mean=25, deviation=5, return_int=True),
        "gender": RandomChoiceGenerator(["M", "F"]),
    }
)

second = PropertyEventGenerator(
    properties={
        "timestamp": DateGenerator(
            center=datetime(2018, 1, 1, 20, 0, 0), deviation=3600
        ),
        "age": NumberGenerator(mean=30, deviation=5, return_int=True),
        "gender": RandomChoiceGenerator(["M", "F"]),
    }
)

background = PropertyEventGenerator(
    properties={
        "timestamp": DateGenerator(
            center=datetime(2018, 1, 1, 15, 0, 0), deviation=8 * 3600
        ),
        "age": NumberGenerator(mean=25, deviation=10, return_int=True),
        "gender": RandomChoiceGenerator(["M", "F"]),
    }
)

composer = EventComposer()
composer.add_generator(first, 1000)
composer.add_generator(second, 1000)
composer.add_generator(background, 200)

pprint(composer.generate(shuffle=True)[:5])
