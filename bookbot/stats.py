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