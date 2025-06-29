def get_book_text(file_path=None):
    if (file_path==None):
        return("Error: filepath not defined")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    text_result = get_book_text(filepath)
main()