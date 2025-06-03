
from stats import get_word_count, get_char_usage
dict_chars ={}
def get_book_text (book_location): # function gets the contents of a book (file)
    with open(book_location) as f:
        book_contents = f.read()
    return book_contents


def main ():

    print(f'{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document')
    print(get_char_usage(get_book_text("books/frankenstein.txt")))
    
    
main()
