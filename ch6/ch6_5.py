def asteroid_collision(asts, x):
    if x >= len(asts) - 1:
        print(str(asts).replace(" 0,",'').replace("[0, ",'[').replace(", 0]",']').replace('[0]','[]'))
        return 0
    
    if asts[x] < 0:
        if asts[x - 1] >= 0 and x > 0:
            if abs(asts[x]) == asts[x - 1]:
                asts[x - 1] = 0
                asts[x] = 0
                asteroid_collision(asts, x - 1)
            elif max(abs(asts[x]),asts[x - 1]) == abs(asts[x]):
                asts[x - 1] = asts[x]
                asts[x] = 0
                asteroid_collision(asts, x - 1)
            else:
                asts[x] = asts[x - 1]
                asts[x - 1] = 0
                asteroid_collision(asts, x - 1)
        else:
            asteroid_collision(asts, x + 1)
            
    elif asts[x] > 0:
        if asts[x + 1] <= 0:
            if abs(asts[x + 1]) == asts[x]:
                asts[x + 1] = 0
                asts[x] = 0
                asteroid_collision(asts, x + 1)
            elif max(abs(asts[x + 1]),asts[x]) == asts[x]:
                asts[x + 1] = asts[x]
                asts[x] = 0
                asteroid_collision(asts, x + 1)
            else:
                asts[x] = asts[x + 1]
                asts[x + 1] = 0
                asteroid_collision(asts, x)
        else:
            asteroid_collision(asts, x + 1)
            
    elif asts[x] == 0:
        if x < len(asts) - 1:
            asteroid_collision(asts, x + 1)
        elif x >= len(asts):
            return 0
    
x = input("Enter Input : ").replace(', ',',').split(",")
x = list(map(int, x))
asteroid_collision(x, 0)