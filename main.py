import time
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
    # open browser and search for the words
    os.system(f"xdg-open 'https://www.bing.com/search?q={get_random_words()}'")