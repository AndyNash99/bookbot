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
    print(f"{count_words()} words found in the document\n")
    char_counts = list(filter(lambda t: t[0].isalpha(), count_chars().items()))
    char_counts.sort(reverse=True, key=lambda t: t[1])
    for key, value in char_counts:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def main():
    read_book("frankenstein")
    report()


main()
