from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_books_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents


def main():
    path_to_book = sys.argv[1]
    book_contents = get_books_text(path_to_book)
    number = num_words(book_contents)
    num_char = num_characters(book_contents)
    sorted_dict = sort_dict(num_char)
    print(f"{number} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()
