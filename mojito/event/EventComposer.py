import csv
import random
from typing import Any, Dict, List, Optional

from .EventGenerator import EventGenerator


class EventComposer:
    def __init__(self):
        self.samples: Dict[int, int] = {}
        self.generators: Dict[int, EventGenerator] = {}

    def add_generator(self, generator: EventGenerator, samples: int):
        self.generators[id(generator)] = generator
        self.samples[id(generator)] = samples

    def remove_generator(self, generator: EventGenerator):
        del self.generators[id(generator)]
        del self.samples[id(generator)]

    def generate(self, shuffle: bool = False) -> List[Dict[str, Any]]:
        total_events = []

        for _id, generator in self.generators.items():
            samples = self.samples[_id]
            events = [generator.generate() for _ in range(samples)]
            total_events.extend(events)

        if shuffle:
            random.shuffle(total_events)
        return total_events

    def to_csv(self, destination: str, shuffle: bool = False, fields: Optional[List[str]] = None):
        events = self.generate(shuffle)
        if fields is None:
            fields = list(events[0].keys())
        with open(destination, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            writer.writeheader()
            writer.writerows(events)
