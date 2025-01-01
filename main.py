from collections import Counter

content = None
book_title = None


def read_book(title):
    global content, book_title
    with open(f"books/{title}.txt") as file:
        book_title = title
        content = file.read()


def count_words():
    words = content.split()
    return len(words)


def count_chars():
    char_counts = Counter(content.lower())
    return char_counts


def report():
    print(f"--- Begin report of books/{book_title}.txt ---")
    print(f"{count_words()} words found in the document")
    print()
    char_counts = count_chars()
    for key, value in char_counts.items():
        print(f"The '{key}' character was found {value} times")


def main():
    read_book("frankenstein")
    report()


main()
