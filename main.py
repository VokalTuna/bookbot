from os import path
import sys
from stats import (
    get_num_words,
    char_count,
    convert_to_list
)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    number_of_words = get_num_words(text)
    character_count = char_count(text)
    converted_list = convert_to_list(character_count)

    print_report(path_to_file,number_of_words, converted_list)

def get_book_text(fpath):
    read_data = ""
    with open(fpath, encoding="utf-8") as f:
        read_data = f.read()
    return read_data

def print_report(book, word_count, list_of_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in list_of_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
