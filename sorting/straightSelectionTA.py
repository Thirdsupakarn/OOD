def selection(l):
    for last in range(len(l)-1, 0, -1):#from last index to 0
        biggest = l[0] # set biggest = first element
        biggest_i = 0 # set index = first index
        for i in range(1, last+1): # from 1 to last find biggest
            if l[i] > biggest: 
                biggest = l[i]
                biggest_i = i 
        l[last], l[biggest_i ] = l[biggest_i], l[last]