file_name = input("Please enter the name of the file you'd like to read: ")


def get_number_of_words(text: str):
    words = text.split()
    return len(words)


def count_chars(text: str):
    chars = {}

    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
            continue
        chars[char] = 1

    return chars


with open(f"books/{file_name}.txt") as f:
    file_contents = f.read()
    num_of_words = get_number_of_words(file_contents)

    print("Begin report of books/frankenstein.txt\n\n")
    print(f"{num_of_words} words found in the document\n")

    char_counts = count_chars(file_contents)

    for k, v in char_counts.items():
        print(f"The '{k}' character was found {v} times")
