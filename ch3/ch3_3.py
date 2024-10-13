def boom(candies,current):
    if len(candies) < 2:
        return False
    return candies[-1] == current == candies[-2]

x = input("Enter Input : ").split()
candies = []
combo = 0
for cur in x:
    if not boom(candies,cur):
        candies.append(cur)
    else:
        combo += 1
        candies.pop()
        candies.pop()

print(len(candies))
print(''.join(reversed(candies)) if candies else "Empty")
if combo > 1:
    print(f'Combo : {combo} ! ! !')