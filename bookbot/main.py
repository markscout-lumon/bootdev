"""
Reads and prints the full text of a book from a local file.
"""

def get_book_text(filepath):
    # Automatically closes the file after reading
    with open(filepath, "r") as f: 
        contents = f.read()
    return contents

def total_words(contents):
    words = contents.split()
    return f"Found {len(words)} total words"

def main():
    # Path is relative to the working directory, not this file
    contents = get_book_text("books/frankenstein.txt")
    print(total_words(contents))

main()