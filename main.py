from stats import get_num_words, count_characters, sort_dict
import sys

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    # filepath = r"./books/frankenstein.txt"
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    char_dict = count_characters(contents)
    dict_list = sort_dict(char_dict)
    print(type(dict_list))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("----------- Character Count ----------")
    for char in dict_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
