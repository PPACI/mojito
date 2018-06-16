import csv
import random
from typing import Any, Dict, List, Optional

from .EventGenerator import EventGenerator


class EventComposer:
    def __init__(self):
        """
        Init an EventComposer used to aggregate multiple event generators
        """
        self.samples: Dict[int, int] = {}
        self.generators: Dict[int, EventGenerator] = {}

    def add_generator(self, event_generator: EventGenerator, samples: int):
        """
        Add an event generator to this composer

        :param event_generator: event generator to add to this composer
        :param samples: number of samples to draw from this generator
        """
        self.generators[id(event_generator)] = event_generator
        self.samples[id(event_generator)] = samples

    def remove_generator(self, generator: EventGenerator):
        """
        Remove a event generator from this composer

        :param generator: event generator to remove from this composer
        """
        del self.generators[id(generator)]
        del self.samples[id(generator)]

    def generate(self, shuffle: bool = True) -> List[Dict[str, Any]]:
        """
        Generate all events from this composer

        :param shuffle: Shuffle events in the resulting list. False by default.
        :return: a list of generated events
        """
        total_events = []

        for _id, generator in self.generators.items():
            samples = self.samples[_id]
            events = [generator.generate() for _ in range(samples)]
            total_events.extend(events)

        if shuffle:
            random.shuffle(total_events)
        return total_events

    def to_csv(self, destination: str, shuffle: bool = False, properties: Optional[List[str]] = None):
        """
        Generate all events from this composer and save them as csv

        :param destination: path for outputted csv
        :param shuffle: Shuffle events in the resulting list. False by default.
        :param properties: List of properties used to order columns in CSV. If not set, columns will have random order.
        """
        events = self.generate(shuffle)
        if properties is None:
            properties = set([key for generator in self.generators.values() for key in generator.keys()])
        with open(destination, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=properties)

            writer.writeheader()
            writer.writerows(events)
