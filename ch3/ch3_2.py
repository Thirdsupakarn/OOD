x = [[int(j) for j in i.split()] for i in input("Enter Input : ").split(",")]
dishes = []

for cur in x:
    if not dishes or dishes[-1][0] >= cur[0]:
        dishes.append(cur)
    else:
        while dishes and dishes[-1][0] < cur[0]:
            print(dishes.pop()[1])
        dishes.append(cur)