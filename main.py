from stats import get_num_words, character_dict, sort_list_dicts 
import sys
def get_book_text(file_path):
    file_text =''
    with open(file_path) as f:
        file_text = f.read()
    return file_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        word_count = get_num_words(text)

        char_dict = character_dict(text)
        dict_list = sort_list_dicts(char_dict)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for d in dict_list:
            if d['char'].isalpha():
                print(f"{d['char']}: {d['num']}")

main()
