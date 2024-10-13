def powerminus1(inp):
    if 2 in inp:
        i = inp.index(2)
        if i == 0:
            return
        inp[i] = 0
        inp[i-1] += 1
        return powerminus1(inp)
    else:
        print(f'{"".join([str(e) for e in inp])}')
        inp[-1] += 1
        return powerminus1(inp)
    
inp = int(input())
if inp < 0:
    print("Only Positive & Zero Number ! ! !")
    exit()

powerminus1([0]*inp)
