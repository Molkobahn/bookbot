def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_text = text.lower()
    num_char = get_num_char(lowered_text)
    print(f"{num_char}")


def get_num_char(lowered_text):
    char_dict = {}
    
    for letter in lowered_text:
        if letter.isalpha():
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
