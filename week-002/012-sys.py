#!/usr/local/bin/python3

# Run me with:
#    cat 012-input.txt | python3 012-sys.py

import sys

for line in sys.stdin:
    print(line.replace("a", "e") \
              .replace("i", "o"))
