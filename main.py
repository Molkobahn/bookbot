import sys
from stats import count_words_in_text

def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words_in_text(text)
    char_count = count_characters(text, count_all=False)
    character_dict = dict_list(char_count)
    character_dict.sort(reverse=True, key=sort_on)
    print_report(num_words, character_dict)
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text, count_all=False):
    char_dict = {}
    for letter in text.lower():
        if count_all or letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def dict_list(char_count):
    list_of_dict = []
    for character in char_count:
        num = char_count[character]
        new_dict = {"character" : character, "num" : num}
        list_of_dict.append(new_dict)
    return list_of_dict

def sort_on(character_dict):
    return character_dict["num"]

def print_report(num_words, character_dict):
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{num_words} words found in the document")
    for x in character_dict:
        print(f"The '{x['character']}' character was found {x['num']} times")
    print("--- End report ---")
    
main()
