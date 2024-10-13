arr = [int(e) for e in input('Enter Input : ').split()]
arr3 = arr.copy()
status = 1
temp = 0
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            temp = j
    if arr3 != arr:
        if (len(arr)-1)-i > 1:
                print(f'{i+1} step : {arr} move[{arr[temp+1]}]')
        elif (len(arr)-1)-i == 1:
            print(f'last step : {arr} move[{arr[temp+1]}]')
    elif status == 1:
        print(f'last step : {arr} move[None]')
        status = 0
    arr3 = arr.copy()