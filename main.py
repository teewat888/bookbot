from stats import get_num_words, get_num_characters,sorted_char, print_result
from sys import argv, exit

def get_book_test(file_path):
    with open(file_path) as f:
        content = f.read()
        return content
def get_report(file_path):
    book_content = get_book_test(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_content)} total words")
    print("--------- Character Count -------")
    print_result(sorted_char(get_num_characters(book_content)))
    print("============= END ===============")
    
def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    if len(argv) == 2:
      try:
        get_report(argv[1])
      except Exception as e:
        print(f"Error: {e}")

main()