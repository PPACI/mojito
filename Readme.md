# Mojito

Mocking temporal data made easy !

There are lot of data mocking framework in Python. But none of them are really oriented toward generating 
statistically homogeneous data, especially temporal event. **Mojito is designed for that !**

## How to use it
```python
from datetime import datetime
from pprint import pprint

from mojito import DateGenerator, EventComposer, FixedValueGenerator, NumberGenerator, PropertyEventGenerator, \
    RandomChoiceGenerator

event1 = PropertyEventGenerator(
        properties={
            "timestamp": DateGenerator(center=datetime(2018, 5, 2, 0, 0, 0), deviation=3 * 3600),
            "age": NumberGenerator(mean=15, deviation=3, return_int=True),
            "gender": RandomChoiceGenerator(['M', 'F']),
            "label": FixedValueGenerator(1)
            })
event2 = PropertyEventGenerator(
        properties={
            "timestamp": DateGenerator(center=datetime(2018, 5, 10, 0, 0, 0), deviation=3 * 3600, skew=0),
            "age": NumberGenerator(mean=30, deviation=3, return_int=True),
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
Mojito use a model where a **PropertyEventGenerator** will be used to generate sample events.
An **Event** is something happening, characterized by the statistical distribution of the sample it represent.
A **Sample** is the generated data. It could represent a visit on your site, or someone buying a specific item
or whatever.
Remember that if you want to generate sample from two statistical distribution, you will have to create two events and
compose them as in the example.
Currently, the main distribution used to generate data is the **Normal distribution** as it's used to represent
lot's of real life distribution.

### EventGenerator
A **PropertyEventGenetator** will be instantiated with a dictionary of {"name":PropertyGenerator}.
This event generator will be at the center of your mocking task as it's describing how event should look like.

### PropertyGenerator
You have access to the following **PropertyGenerator**
* **DateGenerator**
    * Output datetime distributed around the supplied center datetime
    * Distribution is a [Skew Normal](https://en.wikipedia.org/wiki/Skew_normal_distribution)
    * You can pass `skew=0` to have a non skewed normal distribution
    * `scale` is in second, so `deviation=3600` will result in a standard deviation of 1 hours around the provided datetime
* **FixedValueGenerator**
    * Always output the same value
* **RandomChoiceGenerator**
    * Take random choice from a provided list of possibilities
    * You can pass `weights=[a, b]` to weight the list accordingly
* **NumberGenerator**
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
