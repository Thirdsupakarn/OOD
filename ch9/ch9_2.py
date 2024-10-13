lst = [int(e) for e in input('Enter list  of numbers: ').split()]
freq = {}
sorted_dict = {}
for item in lst:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

while freq:
    print(freq,freq.get)
    max_key = max(freq, key=freq.get)
    sorted_dict[max_key] = freq.pop(max_key)

for key, value in sorted_dict.items():
    print(f"number {key}, total: {value}")
