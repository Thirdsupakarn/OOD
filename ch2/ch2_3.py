print("*** Odd Even ***")

def odd_even(type, data, mode):
    result = []
    data = data.split()
    if type == 'S':
        if mode == 'Odd':
            for i in range(0,len(data[0]),2):
                result.append(data[0][i])
        elif mode == 'Even':
            for i in range(1,len(data[0]),2):
                result.append(data[0][i])
        return "".join(result)

    elif type == 'L':
        if mode == 'Odd':
            for i in range(0,len(data),2):
                result.append(data[i])
        elif mode == 'Even':
            for i in range(1,len(data),2):
                result.append(data[i])
        return result

genre,data,mode = input("Enter Input : ").split(",")
print(odd_even(genre,data,mode))