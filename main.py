from stats import get_num_words

def get_book_text(filepath):
    file_output = None
    with open(filepath) as f:
        file_output = f.read()
    return file_output
    
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_contents)
    print(f"Found {word_count} total words")
    
if __name__ == "__main__":
    main()