EVERYTHING_AFTER_BACKSLASH = '(?<=\\\\).+' # regex for anything after a backslash
EVERYTHING_AFTER_DASH = '(?<=-).+' # regex for anything after a dash
STAR_AT_END = '\*$' # regex for a star at the end of a string
ALPHABETICALLY_LAST_STRING = 'ZZZ' # string that comes last alphabetically in a sort

PLAYER_SCORE_ADDITION = 6 # amount to add to PlayerScore to have less negative values
PLAYER_SCORE_EXPONENT = 1.5 # raise positive PlayerScores to this value to make higher scores more significant

NUM_GAMES = {
    '2000-01': 82,
    '2001-02': 82,
    '2002-03': 82,
    '2003-04': 82,
    '2004-05': 82,
    '2005-06': 82,
    '2006-07': 82,
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
    'NJN': 'New Jersey Nets',
    'NOH': 'New Orleans Hornets',
    'NOK': 'New Orleans/Oklahoma City Hornets',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'SEA': 'Seattle SuperSonics',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}

TEAM_CODE = {v: k for k, v in TEAM_NAME.items()}
