def num_words(book_text):
    words = book_text.split()
    number = len(words)
    return number

def num_characters(book_text):
    char_counts ={}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_counts:
            char_counts[lowered] += 1
        else:
            char_counts[lowered] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char":key, "num":value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list