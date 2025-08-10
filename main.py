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

if __name__ == "__main__":
    searches = int(input("Enter the number of searches to perform: "))

    for i in range(searches):
        print(f"Performing search {i + 1}...")
        make_search()
        time.sleep(1)  # wait for 5 seconds before the next search