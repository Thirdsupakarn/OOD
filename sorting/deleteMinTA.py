def delMin(h, last):
    print('delMin', h[0], 'last index = ', last, end = ' ')
    print(h)
    insertEle = h[last]
    h[last] = h[0] #inplace sort the root
    hole = 0
    ls = hole*2+1 # left son indicies
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls+1 
        min = ls if h[ls] < h[rs] else rs # minson index
        if h[min] < insertEle:
            h[hole] = h[min] # promote small son up to hole
            hole = min # going down the tree
            ls = hole*2+1
        else:
            found = True
    h[hole] = insertEle

h = [13,14,16,24,21,19,68,65,26,32,31]
for last in range(len(h)-1, -1, -1):
    delMin(h, last)
    print(h)
    print(h, 0, last)
    print('------------------\n')