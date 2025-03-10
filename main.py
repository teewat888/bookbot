from stats import get_num_words, get_num_characters,sorted_char, print_result

def get_book_test(file_path):
    with open(file_path) as f:
        content = f.read()
        return content
    
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_test("books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    print_result(sorted_char(get_num_characters(get_book_test("books/frankenstein.txt"))))
    print("============= END ===============")
main()