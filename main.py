import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_char_dict

def get_book_text(filepath):
    file_output = None
    with open(filepath) as f:
        file_output = f.read()
    return file_output
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_contents = get_book_text(sys.argv[1])
    word_count = get_num_words(book_contents)
    character_count = get_character_count(book_contents)
    sorted_characters = sort_char_dict(character_count)
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for char in sorted_characters:
        if char["char"].isalpha():
            temp_char = char["char"]
            temp_num = char["num"]
            print(f"{temp_char}: {temp_num}")
    
if __name__ == "__main__":
    main()