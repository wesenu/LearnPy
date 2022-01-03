from collections import Counter

def text_analysis(test_text):
    letter_collection = Counter(test_text)
    return letter_collection