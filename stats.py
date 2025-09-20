def get_num_words(words):
    return len(words.split())

def character_dict(words):
    lower = list(words.lower())
    lower.sort()
    char_dict = {}
    for letter in lower:
        if letter not in char_dict.keys():
            char_dict[letter] = lower.count(letter)
    return char_dict

def sort_list_dicts(char_dict):
    char_count_dict = []
    for key in char_dict.keys():
        char_count_dict.append({'char': key,'num': char_dict[key]})
    def sort_on(items):
        return items['num']
    char_count_dict.sort(reverse=True,key=sort_on)
    return char_count_dict