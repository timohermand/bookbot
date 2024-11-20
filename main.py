def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #chars_sort = sort_on(chars_dict)
    print (f"--- Begin report of {book_path} ---")

    print (f"{num_words} words found in the document")
    print()
    #print(chars_dict)
    #print(chars_sort)
    chars_sort = sort_on(chars_dict)
    print (f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    for letter in dict:
        number=dict[letter]
        if letter.isalpha() :
            print(f"The '{letter}' was found {number} times")
    #return dict["num"]


main()