def get_book_text(filepath):
    with open(filepath, "r") as f:
        contents = f.read()
    return contents