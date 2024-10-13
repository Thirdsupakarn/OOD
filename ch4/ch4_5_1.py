def boom(candies,current):
    if len(candies) < 2:
        return False
    return candies[-1] == current == candies[-2]

def failed_interrupt(candies,current):
    if len(candies) < 3:
        return False
    return candies[-1] == current == candies[-2] == candies[-3]

normal,mirror = input("Enter Input (Normal, Mirror) : ").split()
normal_color = []
mirror_color = []
temp = []
mirror_boom = 0
normal_boom = 0
failed = 0
disturb = []
normal = [e for e in normal]

for cur in normal:
    if not failed_interrupt(temp,cur):
        temp.append(cur)
    else: 
        failed+=1

for cur in mirror:
    if not boom(mirror_color,cur):
        mirror_color.append(cur)
    else:
        mirror_boom += 1
        disturb.append(mirror_color.pop())
        mirror_color.pop()

cur = 0
while cur < len(normal):
    if not boom(normal_color,normal[cur]):
        normal_color.append(normal[cur])
    else:
        if len(disturb) > 0:
            normal.insert(cur,disturb.pop())
            cur+=1
        else:
            break
    cur+=1

normal = "".join(normal)
normal_color = []

for cur in normal:
    if not failed_interrupt(temp,cur):
        temp.append(cur)
    else: 
        failed+=1

for cur in normal:
    if not boom(normal_color,cur):
        normal_color.append(cur)
    else:
        normal_boom += 1
        normal_color.pop()
        normal_color.pop()

print('NORMAL :')
print(len(normal_color))
print(''.join(reversed(normal_color)) if normal_color else 'Empty')
print(f'{normal_boom-failed} Explosive(s) ! ! ! (NORMAL)')
if failed > 0:
    print(f'Failed Interrupted {failed} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(mirror_color))
print(''.join(mirror_color) if mirror_color else 'ytpmE')
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirror_boom}')