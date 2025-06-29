from stats import *

def get_book_text(file_path=None):
    if (file_path==None):
        return("Error: filepath not defined")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text_result = get_book_text(filepath)
    count_words = split_then_count_words(text_result)
    dict_chars, count_chars = char_count(text_result)
    print(f"There are {count_chars} characters in this text file")
    print(f"There are {count_words} words in this text file")
    for char in dict_chars:
        print(f"{char} : {dict_chars[char]}")

main()