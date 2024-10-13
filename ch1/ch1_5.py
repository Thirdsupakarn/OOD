x = int(input("Enter Input : "))
for i in range(x+2):
    for j in range(x+2):
        if j+i < x+1:
            print(".",end='')
        elif j+i >= x+1:
            print("#",end='')
    for k in range(x+2):
        if i == 0 or k == 0 or i == x+1 or k == x+1:
            print("+",end='')
        else:
            print("#",end='')
    print("")

for i in range(x+2):
    for j in range(x+2):
        if i == 0 or j == 0 or i == x+1 or j == x+1:
            print("#",end='')
        else:
            print("+",end='')
    for k in range(x+2):
        if k+i <= x+1:
            print("+",end='')
        elif k+i > x+1:
            print(".",end='')
    print("")
        