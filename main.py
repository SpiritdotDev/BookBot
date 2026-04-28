#imports functions that return a list of all words in a txt 
#file or the entire text file as a string, respectively
from stats import get_book_words, get_book_text,get_book_chars,get_sorted_list
import sys

def report(wordlist,sorted_list,filepath):
    print(
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {len(wordlist)} total words" "\n"
        "--------- Character Count -------"
)
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]} ")
    print(
        "============= END ==============="
    )

# runs both of the above functions
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        wordlist = get_book_words(sys.argv[1])
        count_dict = get_book_chars(sys.argv[1])
        sorted_list = get_sorted_list(count_dict)
        report(wordlist,sorted_list,sys.argv[1])


main()