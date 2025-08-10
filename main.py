import time
import keyboard
import random
import nltk
import os
from nltk.corpus import words
from nltk.corpus import words

def get_random_words():
    nltk.download('words', quiet=True)
    word_list = words.words()
    return ' '.join(random.sample(word_list, 4))

def make_search():
    print("search content")

print(get_random_words())