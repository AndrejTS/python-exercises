def tally(rows):
    teams = {}
    for i in range(len(rows)):
        row = rows[i].split(';')
        teams[row[0]] = {'MP': 0, 'W':0, 'D': 0, 'L': 0, 'P': 0}
        teams[row[1]] = {'MP': 0, 'W':0, 'D': 0, 'L': 0, 'P': 0}
    for i in range(len(rows)):
        row = rows[i].split(';')
        teams[row[0]]['MP'] += 1
        teams[row[1]]['MP'] += 1
        if row[2] == 'win':
            teams[row[0]]['W'] += 1
            teams[row[0]]['P'] += 3
            teams[row[1]]['L'] += 1
        elif row[2] == 'loss':
            teams[row[1]]['W'] += 1
            teams[row[1]]['P'] += 3
            teams[row[0]]['L'] += 1
        elif row[2] == 'draw':
            teams[row[0]]['D'] += 1
            teams[row[0]]['P'] += 1
            teams[row[1]]['D'] += 1
            teams[row[1]]['P'] += 1

    def sorter(team):
        return (team[1]['P'] * (-1), team[0])

    teams = sorted(teams.items(), key=sorter)
    outcome = []
    outcome.append("Team" + " " * 27 + "| MP |  W |  D |  L |  P")
    separator = ' |  '
    for team in teams:
        outcome.append(
            f"{team[0][0:31]:31}|  "
            f"{team[1]['MP']}{separator}"
            f"{team[1]['W']}{separator}"
            f"{team[1]['D']}{separator}"
            f"{team[1]['L']}{separator}"
            f"{team[1]['P']}"
        )

    return outcome

