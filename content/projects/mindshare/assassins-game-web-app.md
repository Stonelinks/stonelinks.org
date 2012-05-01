#Assassins (WebApp)

<hr>

<b>Guest at 2010-05-03 23:30:22:</b><br /><br />

Simple web app to automate the task of running real-life assassins games* by (optimally) assigning aliases, ranking players, giving players several ways to confirm kills (email/text/log-in) and offering team/group-based support. Also, messaging all members when someone is assassinated, etc.

DATA MODELS:

- Team
    - has_many Players
- Player
    - belongs_to Team
    - has_one Target (another Player)
    - has_one Assassin (another Player)
    - other variables: status (alive/dead/deadlined), deadline (time remaining before next kill must be completed)

*see http://en.wikipedia.org/wiki/Assassin_%28game%29
