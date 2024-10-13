def A2X2A(inp,base,cur,reverse):
    if base <= inp and reverse == ord('A')-1:
        if cur <= base:
            print(chr(cur),end='')
            A2X2A(inp,base,cur+1,reverse)
        elif cur > base:
            print()
            A2X2A(inp,base+1,ord('A'),reverse)        
    elif inp > reverse+1:
        if cur < inp:
            print(chr(cur),end='')
            A2X2A(inp,base,cur+1,reverse)
        elif cur >= inp:
            print()
            A2X2A(inp-1,base,ord('A'),reverse)

inp = ord(input("Enter input: ").upper())
base = ord('A')
cur = ord('A')
reverse = ord('A')-1
A2X2A(inp,base,cur,reverse)