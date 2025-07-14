import sys
from stats import get_word_count, get_char_usage, get_sorted_chars, get_book_text
arg = ""
dict_chars = {}
listed_dicts = []

def main ():
    arg = sys.argv
    if len(arg) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    else:
        dict_chars = (get_char_usage(get_book_text(arg[1])))
        for char in dict_chars:
            listed_dicts.append({"char":char,"num":dict_chars[char]})
        
        listed_dicts.sort(reverse=True,key=get_sorted_chars)

        print("============ BOOKBOT ============")
        print("Analyzing book found at ...")
        print("----------- Word Count ----------")
        print(f'Found {get_word_count(get_book_text(arg[1]))} total words')
        print("--------- Character Count -------")
        for word in listed_dicts:
            if word['char'].isalpha():
                print(f'{word['char']}: {word['num']}')
        print("============= END ===============")
   
    
    
main()
