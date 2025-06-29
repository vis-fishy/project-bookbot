def split_then_count_words(text):
    new_list = text.split()
    return len(new_list)

def char_count(raw_text):
    passed_char_set = set()
    passed_char = "abcdefghijklmnopqrstuvwxyz"
    for char in passed_char:
        passed_char_set.add(char)
    
    words_raw_text = raw_text.split()
    char_raw_text = []
    for word in words_raw_text:
        for char in word:
            char_raw_text.append(char.lower())
    char_raw_text.sort()

    passed_char_count = 0
    char_check_set = set()
    passed_dict = {}
    for char in char_raw_text:
        if (char in passed_char):
            if (not(char in char_check_set)):
                char_check_set.add(char)
                passed_char_count += 1
                passed_dict[char] = 1
            else:
                passed_char_count += 1
                passed_dict[char] += 1
    return passed_dict, passed_char_count