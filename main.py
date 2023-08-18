def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")
    
    book_text = get_book_text(book_path)
    print(f"{get_num_words(book_text)} words found in the document")
    
    letters = get_num_letters(book_text)
    letter_list = list(letters.items())
    letter_list.sort(key=lambda x: x[1], reverse=True)

    print()
    for ltr_tup in letter_list:
        if ltr_tup[0].isalpha():
            print(f"The '{ltr_tup[0]}' character was found {ltr_tup[1]} times")
    print("--- End report ---")

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    dict = {}

    for l in text.lower():
        if not l in dict: dict[l] = 0
        dict[l] += 1
    
    return dict
    
main()