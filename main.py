def get_book_text(filepath):
    file_output = None
    with open(filepath) as f:
        file_output = f.read()
    return file_output

def get_num_words(book_contents):
    words = []
    words = book_contents.split()
    word_count = 0
    
    for word in words:
        word_count += 1
    
    return word_count
    
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_contents)
    print(f"Found {word_count} total words")
    
if __name__ == "__main__":
    main()