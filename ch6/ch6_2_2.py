def length(txt):
    if txt == '':
        return 0
    elif txt[1::] == '':
        print(f'{txt}*')
        return 1
    else:
        print(f'{txt[0]}*{txt[1]}~',end='')
        return 2+length(txt[2::])


print("\n",length(input("Enter Input : ")),sep="")