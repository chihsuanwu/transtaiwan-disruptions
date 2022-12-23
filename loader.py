""" Read all disruptions from disruptions folder """

import os
import yaml

def read_disruption(op: str) -> list[dict]:
    # check if file exists
    path = f'disruptions/{op}.yml'

    if not os.path.exists(path):
        return []

    with open(path, encoding='utf-8') as file:
        disruption = yaml.safe_load(file)

    return disruption
