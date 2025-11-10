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
def sort_on(chars):
    return chars["num"]

def sort_char_dict(character_dict):
    sorted_list = []

    for char in character_dict:
        temp_dict = {"char": char, "num": character_dict[char]}
        sorted_list.append(temp_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
        
    return sorted_list