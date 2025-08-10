import time
import random
import nltk
import os
import sys
import webbrowser
from nltk.corpus import words

def get_random_words():
    nltk.download('words', quiet=True)
    word_list = words.words()
    return ' '.join(random.sample(word_list, 4))

def make_search():
    query = get_random_words()
    url = f"https://www.bing.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    searches = int(input("Enter the number of searches to perform: "))
    time_lag = int(input("Enter the time lag between searches (in seconds): "))
    if time_lag < 1:
        print("Time lag must be at least 1 second.")
        exit(1)
    print(f"Performing {searches} searches with a time lag of {time_lag} seconds...")

    for i in range(searches):
        print(f"Performing search {i + 1}...")
        make_search()
        time.sleep(time_lag)