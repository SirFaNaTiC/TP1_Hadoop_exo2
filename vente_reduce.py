#!/usr/bin/env python3

import sys

# Initialize a dictionary to count occurrences of each word
word_count = {}

# Read input from STDIN
for line in sys.stdin:
    # Split the input line into word and count
    word, count = line.strip().split('\t', 1)
    try:
        count = int(count)
        # Increment the count for the word
        word_count[word] = word_count.get(word, 0) + count
    except ValueError:
        # Ignore lines where the count is not an integer
        continue

# Write the word counts to STDOUT
for word, count in word_count.items():
    print(f"{word}\t{count}")