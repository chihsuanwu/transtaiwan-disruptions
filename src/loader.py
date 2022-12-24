""" Read all disruptions from disruptions folder """

import os
import yaml

import const

DIR = 'disruptions'

def read_disruption(op: str) -> list[dict]:
    # check if file exists
    path = f'{DIR}/{op}.yml'

    if not os.path.exists(path):
        return []

    with open(path, encoding='utf-8') as file:
        try:
            disruption = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
            return None

    return disruption


def check_directory() -> bool:
    if not os.path.exists(DIR):
        print(f'Directory {DIR} does not exist')
        return False

    # check if all files name is valid
    files = os.listdir(DIR)

    invalid_files = set(files) - set(map(lambda x: f'{x}.yml', const.operator))
    if invalid_files:
        print(f'Invalid files {invalid_files}')
        return False

    return True