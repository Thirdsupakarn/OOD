class Queue:
    def __init__(self) -> None:
        self.items = []
        
    def __str__(self):
        return ' '.join(self.items)
    
    def Enqueue(self,items):
        self.items.insert(0, items)
        
    def Dequeue(self):
        return self.items.pop(0) if self.size() != 0 else 'Empty'
    
    def size(self):
        return len(self.items)
    
    def reverse(self):
        return self.items.reverse()
    
def monitor(normal_color, normal_boom, failed, mirror_color, mirror_boom):
    print('NORMAL :')
    print(len(normal_color))
    print(''.join(str(x) for x in reversed(normal_color)) if len(normal_color) != 0 else 'Empty')
    print(f'{normal_boom} Explosive(s) ! ! ! (NORMAL)')
    
    if failed != 0:
        print(f'Failed Interrupted {failed} Bomb(s)')
        
    print('------------MIRROR------------')
    print(': RORRIM')
    print(len(mirror_color))
    mirror_color.reverse()

    print(''.join(str(x) for x in mirror_color) if len(mirror_color) != 0 else 'ytpmE')
    print(f'(RORRIM) ! ! ! (s)evisolpxE {mirror_boom}')

normal_color, mirror_color = input('Enter Input (Normal, Mirror) : ').split()
normal_color = list(normal_color)
mirror_color = list(mirror_color)
mirror_color.reverse()

bq, bomb_mirror_color, mirror_boom = Queue(), [], 0
for i, data in enumerate(mirror_color):
    bomb_mirror_color.append(data)
    if len(bomb_mirror_color) > 2:
        if bomb_mirror_color[-1] == bomb_mirror_color[-2] == bomb_mirror_color[-3]:
            bq.Enqueue(data)
            mirror_boom += 1
            for a in range(3):
                bomb_mirror_color.pop()
                
bq.reverse()
bomb_normal_color, normal_boom, failed = [], 0, 0
for i, data in enumerate(normal_color):
    bomb_normal_color.append(data)
    if len(bomb_normal_color) > 2:
        if bomb_normal_color[-1] == bomb_normal_color[-2] == bomb_normal_color[-3]:
            bq_pop = bq.Dequeue()
            if data == bq_pop:
                for a in range(2):
                    bomb_normal_color.pop()
                failed += 1
            elif bq_pop == 'Empty':
                for a in range(3):
                    bomb_normal_color.pop()
                normal_boom += 1
            else:
                bomb_normal_color.insert(-1, bq_pop)

monitor(bomb_normal_color, normal_boom, failed, bomb_mirror_color, mirror_boom)