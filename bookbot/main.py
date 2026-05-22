"""
Reads and prints the full text of a book from a local file.
"""
from stats import total_words, total_chars, chars_dict_to_sorted_list


def get_book_text(filepath):
    # Automatically closes the file after reading
    with open(filepath, "r") as f: 
        contents = f.read()
    return contents



def main():
    # Path is relative to the working directory, not this file
    contents = get_book_text("books/frankenstein.txt")

    word_count = total_words(contents)
    char_counts = total_chars(contents)
    sorted_list = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()