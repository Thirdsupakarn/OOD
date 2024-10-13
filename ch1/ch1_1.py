print("*** Converting hh.mm.ss to seconds ***")
h,m,s = [int(e) for e in input("Enter hh mm ss : ").split()]
result = ('{:,}'.format((h*3600)+(m*60)+s)) 
if m >= 60 or m < 0:
    print(f"mm({m}) is invalid!")
    exit()
if h >= 60 or h < 0:
    print(f"hh({h}) is invalid!")
    exit()
if s >= 60 or s < 0:
    print("ss({s})is invalid!")
    exit()
    
print(f'{h:02}:{m:02}:{s:02} = {result} seconds')