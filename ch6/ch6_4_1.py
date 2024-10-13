def pantip(k, n, arr, path):
    total = 0
    if arr == []:
        return total
    
    if arr[0] + n > k:
        plan = pantip(k, n, arr[1:], path)
        if plan is not None:
            total += plan
    elif arr[0] + n < k:
        path.append(arr[0])
        plan = pantip(k, arr[0] + n, arr[1:], path)
        if plan is not None:
            total += plan
        path.pop()
        plan = pantip(k, n, arr[1:], path)
        if plan is not None:
            total += plan
    elif arr[0] + n == k:
        path.append(arr[0])
        total += 1
        print(str(path).replace('[','').replace(']','').replace(',',''))
        path.pop()
        plan = pantip(k, n, arr[1:], path)
        if plan is not None:
            total += plan
        return total
    
        

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))