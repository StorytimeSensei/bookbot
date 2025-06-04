
from stats import get_word_count, get_char_usage, get_sorted_chars
dict_chars = {}
listed_dicts = []
def get_book_text (book_location): # function gets the contents of a book (file)
    with open(book_location) as f:
        book_contents = f.read()
    return book_contents


def main ():

    dict_chars = (get_char_usage(get_book_text("books/frankenstein.txt")))
    for char in dict_chars:
        listed_dicts.append({"char":char,"num":dict_chars[char]})
    listed_dicts.sort(reverse=True,key=get_sorted_chars)

    print(f'{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document')
    print(listed_dicts)
    

    
    
main()
