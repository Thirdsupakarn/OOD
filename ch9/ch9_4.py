inp = input("Enter Input : ").split()
lst = []
for x in inp:
    for y in x:
        if y.isalpha():
            lst.append([y, x])
            break
        
for x in range(len(lst)):
    changed = False
    for y in range(0, len(lst)-x-1):
        if ord(lst[y][0]) > ord(lst[y+1][0]):
            lst[y], lst[y+1] = lst[y+1], lst[y]
            changed = True
    if changed == False:
        break
for x in lst:
    print(x[1], end=" ")