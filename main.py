import fitz
import re


def main():
    found_kw = []
    kw = get_kw("keywords")
    text = extract_text("sample2.pdf")
    for word in kw:
        if is_word_in_text(word, str(text)):
            found_kw.append(word)
    print(found_kw)


def get_kw(file_name):
    kw = []
    with open(file_name) as file:
        for line in file:
            kw.append(line.lower().strip())
    return kw


def extract_text(pdf_name):
    doc = fitz.open(pdf_name)
    text = ""
    for page in doc:
        text += page.get_text()
    words = text.splitlines()
    return words


def is_word_in_text(word, text):
    """
    Check if a word is in a text.

    Parameters
    ----------
    word : str
    text : str

    Returns
    -------
    bool : True if word is in text, otherwise False.

    Examples
    --------
    is_word_in_text("Python", "python is awesome.")
    True

    is_word_in_text("Python", "camelCase is pythonic.")
    False

    is_word_in_text("Python", "At the end is Python")
    True
    """
    if "+" in word:
        word = re.escape(word)
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)
    return bool(matches)


if __name__ == "__main__":
    main()
