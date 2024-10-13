print("*** Election ***")
input("Enter a number of voter(s) : ")
x = [int(e) for e in input().split()]
winner = []
high = 0
if all(i<0 for i in x):
    print("*** No Candidate Wins ***")
    exit()
for i in x:
    if 0 < i <= 20:
        if high < x.count(i):
            high = x.count(i)
        elif high == x.count(i) and i not in winner:
            winner.append(i)
for i in winner:
    print(i,end=' ')