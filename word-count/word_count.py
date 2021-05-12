import re
from collections import  Counter


def count_words(sentence):
    words = re.findall("[a-z]+'[a-z]|[a-z0-9]+", sentence.lower())
    return Counter(words)

