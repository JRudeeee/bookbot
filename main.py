def get_book_text(filepath):
    file_output = None
    with open(filepath) as f:
        file_output = f.read()
    return file_output
    
def main():
    output = get_book_text("books/frankenstein.txt")
    print(output)
    
if __name__ == "__main__":
    main()