"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    word_list = []

    def __init__(self, location):
        self.location = location
        WordFinder.generate(self)

    def generate(self):
        with open(self.location) as file:
            words = file.read()
            WordFinder.word_list = words.split()
        print(f"{len(WordFinder.word_list)} words read")

    def random(self):
        print(random.choice(WordFinder.word_list))

wr = WordFinder('words.txt')
wr.random()

"""
class WordFinder:
    ...1
"""
