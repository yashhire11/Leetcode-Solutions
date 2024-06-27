#!/bin/bash

# Check if the file exists
if [[ ! -f words.txt ]]; then
  echo "File words.txt not found!"
  exit 1
fi

# Read the file, replace multiple spaces with newlines, sort the words, count unique occurrences, and sort by frequency
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'

# Explanation:
# tr -s ' ' '\n' < words.txt    # Replace multiple spaces with newlines to have one word per line
# sort                          # Sort the words alphabetically
# uniq -c                       # Count unique words, prefixing the count
# sort -nr                      # Sort the counts numerically in descending order
# awk '{print $2, $1}'          # Print the word followed by its count
