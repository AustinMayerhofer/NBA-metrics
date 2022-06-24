EVERYTHING_AFTER_BACKSLASH = '(?<=\\\\).+' # regex for anything after a backslash
EVERYTHING_AFTER_DASH = '(?<=-).+' # regex for anything after a dash
STAR_AT_END = '\*$' # regex for a star at the end of a string
ALPHABETICALLY_LAST_STRING = 'ZZZ' # string that comes last alphabetically in a sort

PLAYER_SCORE_ADDITION = 6 # amount to add to PlayerScore to have less negative values
PLAYER_SCORE_EXPONENT = 1.5 # raise positive PlayerScores to this value to make higher scores more significant
NBA_MIN_GAMES_PCT = 0.6 # percentage of NBA games a player needs to play to qualify for a season
ABA_MIN_GAMES_PCT = 0.6 # percentage of ABA games a player needs to play to qualify for a season


NBA_NUM_GAMES = {
    '1970-71': 82,
    '1971-72': 82,
    '1972-73': 82,
    '1973-74': 82,
    '1974-75': 82,
    '1975-76': 82,
    '1976-77': 82,
    '1977-78': 82,
    '1978-79': 82,
    '1979-80': 82,
    '1980-81': 82,
    '1981-82': 82,
    '1982-83': 82,
    '1983-84': 82,
    '1984-85': 82,
    '1985-86': 82,
    '1986-87': 82,
    '1987-88': 82,
    '1988-89': 82,
    '1989-90': 82,
    '1990-91': 82,
    '1991-92': 82,
    '1992-93': 82,
    '1993-94': 82,
    '1994-95': 82,
    '1995-96': 82,
    '1996-97': 82,
    '1997-98': 82,
    '1998-99': 50,
    '1999-00': 82,
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

NBA_MIN_GAMES = {k: v * NBA_MIN_GAMES_PCT for k, v in NBA_NUM_GAMES.items()}

ABA_NUM_GAMES = {
    '1967-68': 78,
    '1968-69': 78,
    '1969-70': 84,
    '1970-71': 84,
    '1971-72': 84,
    '1972-73': 84,
    '1973-74': 84,
    '1974-75': 84,
    '1975-76': 83
}

ABA_MIN_GAMES = {k: v * ABA_MIN_GAMES_PCT for k, v in ABA_NUM_GAMES.items()}

# some teams like Charlotte use both 'CHH' and 'CHO' for different seasons, can't have multiple 'Charlotte Hornets' keys in TEAM_CODE dict
# for workaround, see use_unique_team_code() in data_cleaning.ipynb
TEAM_NAME = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BRK': 'Brooklyn Nets',
    'BUF': 'Buffalo Braves',
    'CAP': 'Capital Bullets',
    'CAR': 'Carolina Cougars',
    'CHI': 'Chicago Bulls',
    'CHA': 'Charlotte Bobcats',
    'CHO': 'Charlotte Hornets',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'DNR': 'Denver Rockets',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'KCK': 'Kansas City Kings',
    'KCO': 'Kansas City-Omaha Kings',
    'KEN': 'Kentucky Colonels',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'MMS': 'Memphis Sounds',
    'MMT': 'Memphis Tams',
    'NJN': 'New Jersey Nets',
    'NOH': 'New Orleans Hornets',
    'NOJ': 'New Orleans Jazz',
    'NOK': 'New Orleans/Oklahoma City Hornets',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'NYN': 'New York Nets',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'SDA': 'San Diego Conquistadors',
    'SDC': 'San Diego Clippers',
    'SDS': 'San Diego Sails',
    'SEA': 'Seattle SuperSonics',
    'SSL': 'Spirits of St. Louis',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'UTS': 'Utah Stars',
    'VAN': 'Vancouver Grizzlies',
    'VIR': 'Virginia Squires',
    'WAS': 'Washington Wizards',
    'WSB': 'Washington Bullets'
}

TEAM_CODE = {v: k for k, v in TEAM_NAME.items()}
