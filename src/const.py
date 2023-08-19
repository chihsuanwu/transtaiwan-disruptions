
operator = [ 'tra', 'thsr', 'trtc', 'krtc', 'tymc', 'tmrt', 'klrt', 'ntdlrt' ]

LINES = {
    'trtc': [
        'R', 'G', 'O', 'Y', 'BL', 'BR', 'R22A', 'G03A'
    ],
    'krtc': [
        'R', 'O'
    ],
    'tymc': [
        'A'
    ],
    'tmrt': [
        'G'
    ],
    'klrt': [
        'C'
    ],
    'ntdlrt': [
        'V'
    ]
}

DISRUPTION_KEYS = [
    'AlertID',
    'Title',
    'Description',
    'Status',
    'Scope',
    'direction',
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