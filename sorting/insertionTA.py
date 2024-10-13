def insertion(l):
    for i in range(1, len(l)): #from index 1 to last index
        iEle = l[i] #assign insertElement
        for j in range(i, -1, -1):
            if l[j-1] > iEle and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break


l1 = [32,26,2,15,264,-183,10,0,20,-142,-1]
insertion(l1)
print(l1)
