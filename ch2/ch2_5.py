print("*** TorKham HanSaa ***")

x = input("Enter Input : ").split(",")
result = []
count = -1
for i in x:
    if i[0] == 'P':
        i = i.replace("P ","")
        if result == []:
            result.append(i)
            print(f"'{i}' -> {result}")
        else:
            j = result[count]
            if i[0].upper() == j[len(j)-2].upper() and i[1].upper() == j[len(j)-1].upper(): 
                result.append(i)
                print(f"'{i}' -> {result}")
            else:
                print(f"'{i}' -> game over")
                exit()
        count+=1
    elif i[0] == 'R':
        result = []
        count = -1
        print("game restarted")
    elif i[0] == 'X':
        exit()
    else:
        print(f"'{i}' is Invalid Input !!!")
        exit()