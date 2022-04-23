# Raw Data Testing

## Player Per Game
- columns has Rk,Player,Pos,Age,Tm,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS
- Player has a player ID (after backslash \\), and if I have a list of all the player IDs, it must be in that list
- values that shouldn't be negative, are >= 0, or NaN
- values that should be capped, like a %, are at max or NaN
- Age is between 10 and 100
- Tm is a team that actually exists, or TOT
- NaNs only exist in FG%, 3P%, 2P%, eFG%, FT%

## Advanced Player Stats
- same number of rows in per game stats and advanced stats
- columns has Rk,Player,Pos,Age,Tm,G,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%,OWS,DWS,WS,WS/48,OBPM,DBPM,BPM,VORP, and 2 unnamed columns
- Player has a player ID (after backslash \\), and if I have a list of all the player IDs, it must be in that list
- values that shouldn't be negative, are >= 0, or NaN
- values that should be capped, like a %, are at max or NaN
- Age is between 10 and 100
- Tm is a team that actually exists, or TOT

## Teams
- columns are Rk,Team,Overall,Home,Road,E,W,A,C,SE,NW,P,SW,Pre,Post,≤3,≥10,Dec,Jan,Feb,Mar,Apr,May
- for W-L columns, all cells formatted as {int}-{int}


## Ordering of Data that has to be read in
1. Teams
2. Player Per Game

# Installation
- kernel uses python 3.8.9
