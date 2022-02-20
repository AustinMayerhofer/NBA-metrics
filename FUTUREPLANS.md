# raw data testing

- columns are Rk,Player,Pos,Age,Tm,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS
- values that shouldn't be negative, are >= 0, or NaN
- values that should be capped, like a %, are at max or NaN
- Age is between 10 and 100
- Tm is a team that actually exists, or TOT
- NaNs only exist in FG%, 3P%, 2P%, eFG%, FT%
