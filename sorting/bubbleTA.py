def bubble(l):
    for last in range(len(l)-1, 0,-1):#from last index to 0
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] #swap is true
                swaped = True
        if not swaped:
            break