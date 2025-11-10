def get_num_words(book_contents):
    words = []
    words = book_contents.split()
    word_count = 0
    
    for word in words:
        word_count += 1
    
    return word_count
