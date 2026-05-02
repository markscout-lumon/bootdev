def get_book_text(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
    return contents

def main():
    contents = get_book_text("books/frankenstein.txt")
    print(contents)

main()