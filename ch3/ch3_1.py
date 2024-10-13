x = input("Enter Input : ").split(",")
result = []
count = -1
for i in x:
    if i[0] == 'A':
        i = i.replace("A ","")
        result.append(i)
        print(f"Add = {i} and Size = {len(result)}")
        count +=1
    else:
        if len(result) > 0:
            print(f"Pop = {result.pop()} and Index = {count}")
            count -=1
        else:
            print(-1)

print(f"Value in Stack = {' '.join(result)}" if result else "Value in Stack = Empty")