x = input("Enter Input : ").split(",")
result = []
count = 0
for i in x:
    if i[0] == 'E':
        i = i.replace("E ","")
        result.append(i)
        print(f"Add {i} index is {count}")
        count +=1
    else:
        if len(result) > 0:
            print(f"Pop {result.pop(0)} size in queue is {len(result)}")
            count -=1
        else:
            print(-1)

print(f"Number in Queue is :  {result}" if result else "Empty")