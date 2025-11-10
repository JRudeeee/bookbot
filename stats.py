def get_num_words(book_contents):
    words = []
    words = book_contents.split()
    word_count = 0
    
    for word in words:
        word_count += 1
    
    return word_count

def get_character_count(book_contents):
    book_contents = book_contents.lower()
    characters = {}
    for char in book_contents:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters