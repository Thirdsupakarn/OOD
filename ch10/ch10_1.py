unordered_words_and_meanings = {
    'watermelon': 'A Large fruit',
    'nectarine': 'Similar to a peach.',
    'mango': 'Tropical fruit.',
    'kiwi': 'Small fruit.',
    'vanilla': 'Used in baking.',
    'fig': 'Chewy skin.',
    'pear': 'Sweet fruit.',
    'cherry': 'Red fruit.',
    'strawberry': 'Tiny seeds.',
    'quince': 'Tart flavor.',
    'ugli fruit': 'Hybrid citrus.'
}

defalut_meaning = '(Default) A fruit.'

def print_updated_dict(updated_dict):
    print("(END) Updated dictionary:")
    for i in range(len(updated_dict)):
        if i != 0:
            print(", ", end="")
        print(f"{i}: {updated_dict[i]}", end = "")
    print()

def transposition_search(keys):
    updated_dict = [key for key in unordered_words_and_meanings.keys()]
    summary = {}
    for i in range(len(keys)):
        time = 1
        for word in updated_dict:
            if keys[i] == word:
                print(f"({i+1}) Word '{word}' found ({time+1} seconds): {unordered_words_and_meanings[word]}")
                if time-1 > 0:
                    updated_dict[time-2], updated_dict[time-1] = updated_dict[time-1], updated_dict[time-2]
                if word not in summary.keys():
                        summary[word] = time-1
                break
            time += 1
        else:
            unordered_words_and_meanings[keys[i]] = defalut_meaning
            print(f"({i+1}) Word '{keys[i]}' added ({time+1} seconds): {unordered_words_and_meanings[keys[i]]}")
            updated_dict.append(keys[i])
            summary[keys[i]] = None
    print_updated_dict(updated_dict)
    index_summary(summary, updated_dict)

def index_summary(summary, dictionary):
    print("(SUMMARY OF INDEX CHANGES):")
    for key in summary.keys():
        for i in range(len(dictionary)):
            if dictionary[i] == key:
                print(f"{key}: {summary[key]} -> {i}")
                break

words = [word.strip().lower() for word in input("Enter a word to search for: ").split(",")]
transposition_search(words)