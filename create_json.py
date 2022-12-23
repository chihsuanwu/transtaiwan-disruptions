import json

from loader import read_disruption


def main():
    operator = [ 'tra', 'thsr', 'trtc', 'krtc', 'tymc', 'tmrt', 'klrt', 'ntdlrt' ]

    all_disruptions = {}
    for op in operator:
        data = read_disruption(op)
        all_disruptions[op] = data

    with open('disruptions.json', 'w', encoding='utf-8') as file:
        json.dump(all_disruptions, file, ensure_ascii=False)

if __name__ == '__main__':
    main()