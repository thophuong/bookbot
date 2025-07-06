def get_num_words(contents):
    words_list = contents.split()
    return len(words_list)

def count_characters(contents) -> dict:
    from collections import Counter
    return dict(Counter(contents.lower()))

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    dict_list = []
    for k in char_dict:
        if k.isalpha():
            dict_list.append({"char":k, "num": char_dict[k]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
