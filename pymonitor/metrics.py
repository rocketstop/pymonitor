from typing import Dict
from pymonitor.utils import get_attribute
from pymonitor.utils import dict_to_string

import psutil


def report_memory_metrics() -> Dict:
    ram = psutil.virtual_memory()
    attributes = ('total', 'available', 'used', 'percent')
    values = {}

    for attribute in attributes:
        values[attribute] = get_attribute(ram, attribute, False)

    return values


if __name__ == "__main__":
    metrics: Dict = report_memory_metrics()
    print(metrics)
    print(metrics.keys())
    print(dict_to_string(metrics))
