x = [int(e) for e in input("Enter Your List : ").split()]
result = []
if len(x) < 3:
    print("Array Input Length Must More Than 2")
    exit()
if all(e for e in x) == 0:
    result = [[0, 0, 0]]
else:
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                if x[i]+x[j]+x[k] == 0 :
                    result.append([x[i],x[j],x[k]])

print(result)
