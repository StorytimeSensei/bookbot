def get_word_count(book): # get the total word count of the book
    num_words = 0
    words =[]
    words = book.split()
    for w in words:
        num_words += 1
    return num_words

def  get_char_usage(book): # gets the count of each individual character within a book
    char_count = {}
    for character in book:
        char = character.lower()
        if char not in char_count:
            char_count[char] = 1
        else: char_count[char] += 1
    return char_count

#def get_sorted_chars(char_dictionary):
#    sorted_chars = []
#    for char in char_dictionary:
#        sorted_chars.append(char)
#    return sorted_chars


