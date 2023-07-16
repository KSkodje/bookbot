def main():
    file_path = "./books/frankenstein.txt"
    text = read_file(file_path)
    words = word_count(text)
    chars = letters_count(text)
    print_chars_report(file_path, words, chars)

def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    wordcount = len(text.split())
    return wordcount

def letters_count(text):
    letters = [letter for letter in text.lower()]
    char_count = {}
    for l in letters:
        if l in char_count:
            char_count[l] += 1
        else:
            char_count[l] = 1
    return char_count

def print_chars_report(file, word_count, chars_dict):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document\n")
    sorted_letters = sorted([l for l in chars_dict.keys()])
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"The '{letter}' was found {chars_dict[letter]} times")
    print(f"--- End report ---")

main()