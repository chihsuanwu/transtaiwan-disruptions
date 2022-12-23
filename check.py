""" This file check all the disruption data in disruption folder has correct format. """

from datetime import datetime

from loader import read_disruption

DISRUPTION_KEYS = [
    'AlertID',
    'Title',
    'Description',
    'Status',
    'Scope',
    'Direction',
    'Level',
    'StartTime',
    'EndTime',
]

SCOPE_KEYS = [
    'Stations',
    'Lines',
    'Trains',
    'AllStations',
]


def check_id(disruption: dict) -> bool:
    id = disruption['AlertID']

    if not isinstance(id, str):
        return False

    return True


def check_title(disruption: dict) -> bool:
    title = disruption['Title']

    if not isinstance(title, str):
        return False

    if not 3 < len(title) < 16:
        print(f'Title {title} length should in 4 - 15')
        return False

    return True


def check_description(disruption: dict) -> bool:
    description = disruption['Description']

    if not isinstance(description, str):
        return False

    if not 3 < len(description) < 256:
        print(f'Description {description} length should in 4 - 255')
        return False

    return True


def check_status(disruption: dict) -> bool:
    status = disruption['Status']

    if not isinstance(status, int):
        return False

    if status not in [0, 2, 3, 4]:
        print(f'Status {status} should be 0, 2, 3, 4')
        return False

    return True


def check_scope(disruption: dict) -> bool:
    scope = disruption.get('Scope')

    if not scope:
        return True

    if not isinstance(scope, dict):
        return False

    if scope.get("Stations") and (
        not isinstance(scope["Stations"], list) or
        not all(isinstance(s, str) for s in scope["Stations"])):
        print(f'Scope Stations {scope["Stations"]} should be list[str]')
        return False

    if scope.get("Lines") and (
        not isinstance(scope["Lines"], list) or
        not all(isinstance(l, str) for l in scope["Lines"])):
        print(f'Scope Lines {scope["Lines"]} should be list[str]')
        return False

    if scope.get("Trains") and (
        not isinstance(scope["Trains"], list) or
        not all(isinstance(t, str) for t in scope["Trains"])):
        print(f'Scope Trains {scope["Trains"]} should be list[str]')
        return False

    if scope.get("AllStations") and not isinstance(scope["AllStations"], bool):
        print(f'Scope AllStations {scope["AllStations"]} should be bool')
        return False

    if scope.keys() - set(SCOPE_KEYS):
        print(f'Scope {scope.keys()} should be in {SCOPE_KEYS}')
        return False

    return True


def check_direction(disruption: dict) -> bool:
    direction = disruption.get('Direction')

    if not direction:
        return True

    if not isinstance(direction, int):
        return False

    if direction not in [0, 1, 2]:
        print(f'Direction {direction} should be 0, 1, 2')
        return False

    return True


def check_level(disruption: dict) -> bool:
    level = disruption.get('Level')

    if not level:
        return True

    if not isinstance(level, int):
        return False

    if level not in [1, 2, 3]:
        print(f'Level {level} should be 1, 2, 3')
        return False

    return True


def check_start_time(disruption: dict) -> bool:
    start_time = disruption.get('StartTime')

    if not start_time:
        return True

    return check_time(start_time)


def check_end_time(disruption: dict) -> bool:
    end_time = disruption.get('EndTime')

    if not end_time:
        return True

    return check_time(end_time)


def check_time(time):
    if not isinstance(time, str):
        return False

    if len(time) != 25:
        print(f'Time {time} should be format: yyyy-MM-dd\'T\'HH:mm:sszzz')
        return False

    # Try to parse by format: yyyy-MM-dd'T'HH:mm:sszzz
    try:
        datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
    except ValueError:
        print(f'Time {time} should be format: yyyy-MM-dd\'T\'HH:mm:sszzz')
        return False

    return True


def check_disruption(disruption: dict) -> bool:
    if not isinstance(disruption, dict):
        return False

    if not check_id(disruption):
        print(f'Invalid id: {disruption["AlertID"]}')
        return False

    if not check_title(disruption):
        print(f'Invalid title: {disruption["Title"]}')
        return False

    if not check_description(disruption):
        print(f'Invalid description: {disruption["Description"]}')
        return False

    if not check_status(disruption):
        print(f'Invalid status: {disruption["Status"]}')
        return False

    if not check_scope(disruption):
        print(f'Invalid scope: {disruption["Scope"]}')
        return False

    if not check_direction(disruption):
        print(f'Invalid direction: {disruption["Direction"]}')
        return False

    if not check_level(disruption):
        print(f'Invalid level: {disruption["Level"]}')
        return False

    if not check_start_time(disruption):
        print(f'Invalid start time: {disruption["StartTime"]}')
        return False

    if not check_end_time(disruption):
        print(f'Invalid end time: {disruption["EndTime"]}')
        return False

    if disruption.keys() - set(DISRUPTION_KEYS):
        print(f'Disruption {disruption.keys()} should be in {DISRUPTION_KEYS}')
        return False

    return True


def check_data(op: str) -> bool:
    data = read_disruption(op)

    result = [ (d.get("AlertID"), check_disruption(d)) for d in data ]

    # Check all id is unique
    ids = [ r[0] for r in result ]
    if len(ids) != len(set(ids)):
        print(f'AlertID is not unique: {ids}')
        return False

    for r in result:
        print(f'{op} {r[0]} : {r[1]}')

    return all(r[1] for r in result)


def main():
    oper = ['tra', 'thsr', 'trtc', 'krtc', 'tymc', 'tmrt', 'klrt', 'ntdlrt']

    result = { op: check_data(op) for op in oper }

    for op, r in result.items():
        print(f'{op} : {r}')

    assert all(result.values())


if __name__ == '__main__':
    main()