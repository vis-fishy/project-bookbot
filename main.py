#!C:\Users\user\AppData\Local\Programs\Python\Launcher\py.exe
from stats import *
import sys

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    try:
        #text file name section
        filepath = sys.argv[1]
        text_result = get_book_text(filepath)
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
        sys.exit(0)
    
    except IndexError:
        print("IndexError: filepath not defined")
        print("Usage : py main.py <path_to_file>")
        sys.exit(1)
    
    except Exception as gen:
        print(gen)
        print("Usage : py main.py <path_to_file>")
        sys.exit(1)
main()