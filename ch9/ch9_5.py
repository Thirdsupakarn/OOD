def premierleagueScore(data):
    tab = []
    for team in data:
        temp = []
        team = team.split(',')
        score = int(team[1]) * 3 + int(team[3])
        gd = int(team[4]) - int(team[5])
        temp += [team[0],score,gd]
        tab.append(temp)
    for i in range(1,len(tab)):
        temp = tab[i]
        for k in range(i,-1,-1):
            if temp[1] > tab[k - 1][1] and k > 0:
                tab[k] = tab[k - 1]
            elif temp[1] == tab[k - 1][1] and k > 0:
                if temp[2] > tab[k - 1][2]:
                    tab[k] = tab[k - 1]
                else:
                    tab[k] = temp
                    break
            else:
                tab[k] = temp
                break
    return tab

inp = input('Enter Input : ').split('/')
premierleagueScore = premierleagueScore(inp)
print('== results ==')
for data in premierleagueScore:
    print(f"['{data[0]}', " + "{'points': " + f"{data[1]}" + "}, {" + f"'gd': {data[2]}" + "}]")