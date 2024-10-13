def permutation(l):
    if l == []:
        print("0")
        return 1
    elif 2 in l:
        i = l.index(2)
        if i == 0:
            return 1
        l[i-1] += 1
        l[i] = 0
        return permutation(l)
    else:
        print("".join([str(i) for i in l]))
        l[-1] += 1
        return permutation(l)

n = int(input("Enter Number : "))
if n < 0:
    print("Only Positive & Zero Number ! ! !")
    exit()
permutation([0]*n)