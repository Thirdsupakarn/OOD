def condition(mid, tasks, worker):
    load = [0]*worker
    tasks.sort(reverse=True)
    memo = {}
    
    def recur(idx):
        if idx == len(tasks):
            return True
        state = tuple(load)
        if state in memo:
            return memo[state]
        
        task = tasks[idx]
    
        for i in range(worker):
            if load[i] + task <= mid:
                load[i] += task
                if recur(idx + 1):
                    memo[state] = True
                    return True
                load[i] -= task
            if load[i] == 0:
                break
        memo[state] = False
        return False
    return recur(0)


inp, worker = input("Enter jobs and number of workers : ").split('/')
inp = [int(e) for e in inp.split()]
worker = int(worker)
l, r = max(inp), sum(inp)
while l <= r:
    mid = (l + r) // 2
    if condition(mid, inp, worker):
        r = mid - 1
    else:
        l = mid + 1

print(f"Minimum time to complete jobs with {worker} workers is {l}")
