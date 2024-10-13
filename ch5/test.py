class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ' if current.next else '')
            current = current.next
        print()

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

def radix_sort_linked_list(ll):
    def counting_sort_for_radix(input_list, exp, is_negative):
        output_list = [0] * len(input_list)
        count = [0] * 10

        for i in range(len(input_list)):
            index = abs(input_list[i]) // exp
            count[(index % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = len(input_list) - 1
        while i >= 0:
            index = abs(input_list[i]) // exp
            output_list[count[(index % 10)] - 1] = input_list[i]
            count[(index % 10)] -= 1
            i -= 1

        for i in range(len(input_list)):
            
            input_list[i] = output_list[i]
            print(input_list[i])
            
    max_val = max(ll.to_list(), key=abs)
    exp = 1
    round_num = 1
    while max_val // exp > 0:
        print("------------------------------------------------------------")
        print(f"Round : {round_num}")

        input_list = ll.to_list()
        counting_sort_for_radix(input_list, exp, is_negative=False)

        buckets = [[] for _ in range(10)]
        for num in input_list:
            index = abs(num) // exp % 10
            buckets[index].append(num)

        for i in range(10):
            print(f"{i} : {' '.join(map(str, buckets[i]))}")

        ll.from_list(input_list)
        exp *= 10
        round_num += 1

    print("------------------------------------------------------------")
    print(f"{round_num-1} Time(s)")

    sorted_list = ll.to_list()
    negative_numbers = [num for num in sorted_list if num < 0]
    positive_numbers = [num for num in sorted_list if num >= 0]
    ll.from_list(negative_numbers + positive_numbers)


input_data = list(map(int, input("Enter Input : ").split()))
ll = LinkedList()
for num in input_data:
    ll.append(num)

print("Before Radix Sort : ", end="")
ll.print_list()

radix_sort_linked_list(ll)

print("After Radix Sort : ", end="")
ll.print_list()
