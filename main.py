def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
 
    char_count = count_characters(text, count_all=True)
    print("Character counts:")
    print(char_count)


def count_characters(text, count_all=False):
    char_dict = {}
    for letter in text.lower():
        if count_all or letter.isalpha():
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)
          
          
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
