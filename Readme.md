# Mojito

Mocking temporal data made easy !

There are lot of data mocking framework in Python. But none of them are really oriented toward generating 
statistically homogeneous data, especially temporal event. **Mojito is designed for that !**

## How to use it
```python
from datetime import datetime
from pprint import pprint

from mojito.date.SkewedNormalDateGenerator import SkewedNormalDateGenerator
from mojito.event.EventComposer import EventComposer
from mojito.event.TimestampEventGenerator import TimestampEventGenerator
from mojito.property.FixedValueGenerator import FixedValueGenerator
from mojito.property.RandomChoiceGenerator import RandomChoiceGenerator
from mojito.property.SkewedNormalNumberGenerator import SkewedNormalNumberGenerator

event1 = TimestampEventGenerator(
        timestamp=SkewedNormalDateGenerator(center=datetime(2018, 5, 2, 0, 0, 0), deviation=3 * 3600),
        properties={
            "age": SkewedNormalNumberGenerator(mean=15, deviation=3, return_int=True),
            "gender": RandomChoiceGenerator(['M', 'F']),
            "label": FixedValueGenerator(1)
            })
event2 = TimestampEventGenerator(
        timestamp=SkewedNormalDateGenerator(center=datetime(2018, 5, 10, 0, 0, 0), deviation=3 * 3600, skew=0),
        properties={
            "age": SkewedNormalNumberGenerator(mean=30, deviation=3, return_int=True),
            "gender": RandomChoiceGenerator(['M', 'F'], weights=[2, 1]),
            "label": FixedValueGenerator(0)
            })

composer = EventComposer()
composer.add_generator(event1, 3)  # 3 samples from this generator
composer.add_generator(event2, 2)  # 2 samples from this generator

pprint(composer.generate(shuffle=True))
```
Will output
```python
[{'age': 16.0,
  'gender': 'M',
  'label': 1,
  'timestamp': datetime.datetime(2018, 5, 1, 22, 23, 1, 450298)},
 {'age': 19.0,
  'gender': 'F',
  'label': 1,
  'timestamp': datetime.datetime(2018, 5, 1, 21, 0, 11, 583775)},
 {'age': 30.0,
  'gender': 'M',
  'label': 0,
  'timestamp': datetime.datetime(2018, 5, 9, 22, 57, 30, 441924)},
 {'age': 15.0,
  'gender': 'F',
  'label': 1,
  'timestamp': datetime.datetime(2018, 5, 2, 5, 59, 54, 96498)},
 {'age': 32.0,
  'gender': 'M',
  'label': 0,
  'timestamp': datetime.datetime(2018, 5, 10, 0, 15, 55, 676862)}]
```

## API
Mojito use a model where an **EventGenerator** will be used to generate sample events.
There are two types of generators available :
* Date Generator
    * Used to generate random timestamp
* Property Generator
    * Used to generate multiple properties
### Event
Currently, there is only one way of generating events, and that's with the *TimestampEventGenerator*.
Check the example to see how to instantiate it.  
There are two parameters for this class
* timestamp
    * an instance of a DateGenerator used to draw random timestamp
** properties
    * a dict like `{property_name: instance of PropertyGenerator}`
    * used to draw different property for each generated events

*Note : the special timestamp property will have the name **timestamp***
### Date
You have access to the following **DateGenerator**
* **SkewedNormalDateGenerator**
    * Output datetime distributed around the supplied center datetime
    * Distribution is a [Skew Normal](https://en.wikipedia.org/wiki/Skew_normal_distribution)
    * You can pass `skew=0` to have a non skewed normal distribution
    * `scale` is in second, so `deviation=3600` will result in a standard deviation of 1 hours around the provided datetime
### Property
You have access to the following **PropertyGenerator**
* **FixedValueGenerator**
    * Always output the same value
* **RandomChoiceGenerator**
    * Take random choice from a provided list of possibilities
    * You can pass `weights=[a, b]` to weight the list accordingly
* **SkewedNormalNumberGenerator**
    * Output number distributed around the supplied mean
    * Distribution is a [Skew Normal](https://en.wikipedia.org/wiki/Skew_normal_distribution)
    * You can pass `skew=0` to have a non skewed normal distribution
    * You can pass `return_int=True` to generate *integer* instead of *float*
### Composition
Real models are aggregation of multiple, different, events. To simulate this, you can use the *EventComposer*.
````python
composer = EventComposer()
composer.add_generator(event1, 3)  # 3 samples from this generator
composer.add_generator(event2, 2)  # 2 samples from this generator
````

Add your EventGenerator and the number of wanted generated events from each generator.
You can also remove one with `.remove_generator(event1)`.

* `.generate()` will return you a list of generated events as dictionary
* `.to_csv("output.csv")` will save the generated events as csv, ready for your process !
