#!/usr/bin/python3

import re
import random

def is_good_candidate(word):
    mustHave = "no"
    ascenders = "bdfhkl"
    descenders = "gjpqy"
    diagonals = "krvwxyz"
    rounded = "abcdeghmnopqsu"
    isAcceptableLength = len(word) < 7 and len(word) > 4
    if not isAcceptableLength:
        return False
    
    hasOnlyLowercase = word.islower()
    if not hasOnlyLowercase:
        return False
    
    hasOnlyAlphabeticChars = word.isalpha()
    if not hasOnlyAlphabeticChars:
        return False
    
    hasUniqueLetters = len(set(list(word))) == len(word)
    if not hasUniqueLetters:
        return False
    
    hasMustHave = re.search(f"[{mustHave}]", word)
    if not hasMustHave:
        return False
    
    hasAscenders = re.search(f"[{ascenders}]", word)
    if not hasAscenders:
        return False
    hasDescenders = re.search(f"[{descenders}]", word)
    if not hasDescenders:
        return False
    hasDiagonals = re.search(f"[{diagonals}]", word)
    if not hasDiagonals:
        return False
    hasRounded = re.search(f"[{rounded}]", word)
    if not hasRounded:
        return False
    
    return True

def search_for_words():
    candidates = []
    with open("./english-words/words.txt") as englishDictFile:
        for line in englishDictFile:
            word = line.strip()
            if is_good_candidate(word):
                candidates.append(word)
    lenCandidates = len(candidates)
    randoms = random.sample(candidates, 5)
    print(f"Found {lenCandidates} words.")
    print(f"Here's five random ones: {randoms}")
    
if __name__ == "__main__":
    search_for_words()