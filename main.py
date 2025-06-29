from stats import *

def get_book_text(file_path=None):
    if (file_path == None):
        print("Error: filepath not defined")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text_result = get_book_text(filepath)

    if (filepath != None):
        #text file name section
        string_filepath = filepath.split("/")
        name = ""
        for string in string_filepath:
            if (string[-4:] == ".txt"):
                name = string

        #sorted dictionary section (big - small)        
        count_words = split_then_count_words(text_result)
        dict_chars, count_chars = char_count(text_result)
        sorted_list_dict = dict_to_list_sorted(dict_chars)
        print(f"There are {count_chars} characters in this {name} text file")
        print(f"There are {count_words} words in this {name} text file")
        for item in sorted_list_dict:
            print(f"{item["name"]} : {item["value"]}")

main()