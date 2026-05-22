from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int

def total_words(contents):
    words = contents.split()
    return f"Found {len(words)} total words"

def total_chars(contents):
    lowercase = contents.lower()

    counts = {}

    for char in lowercase:
        if char in counts:
           counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    # return the value used for comparison
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for i in num_chars_dict:
        sorted_list.append({"char": i, "num": num_chars_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list