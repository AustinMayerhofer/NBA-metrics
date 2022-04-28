EVERYTHING_AFTER_BACKSLASH = '(?<=\\\\).+' # regex for anything after a backslash
EVERYTHING_AFTER_DASH = '(?<=-).+' # regex for anything after a dash
ALPHABETICALLY_LAST_STRING = 'ZZZ' # string that comes last alphabetically in a sort

NUM_GAMES = {
    '2007-08': 82,
    '2008-09': 82,
    '2009-10': 82,
    '2010-11': 82,
    '2011-12': 66,
    '2012-13': 82,
    '2013-14': 82,
    '2014-15': 82,
    '2015-16': 82,
    '2016-17': 82,
    '2017-18': 82,
    '2018-19': 82,
    '2019-20': 63,
    '2020-21': 72,
    '2021-22': 82
}

TEAM_NAME = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BRK': 'Brooklyn Nets',
    'CHI': 'Chicago Bulls',
    'CHA': 'Charlotte Bobcats',
    'CHO': 'Charlotte Hornets',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOH': 'New Orleans Hornets',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}

TEAM_CODE = {v: k for k, v in TEAM_NAME.items()}
