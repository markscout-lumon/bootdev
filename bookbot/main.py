"""
Reads and prints the full text of a book from a local file.
"""
from stats import total_words, total_chars, sort_on, chars_dict_to_sorted_list


def get_book_text(filepath):
    # Automatically closes the file after reading
    with open(filepath, "r") as f: 
        contents = f.read()
    return contents


def main():
    # Path is relative to the working directory, not this file
    contents = get_book_text("books/frankenstein.txt")
    print(total_words(contents))
    print(total_chars(contents))
    print(sort_on(contents))
    print(chars_dict_to_sorted_list(contents))

main()