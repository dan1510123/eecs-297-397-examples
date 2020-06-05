#!/usr/local/bin/python3

# Run me with:
#  cat 013-input.txt | python3 013-sys.py

import sys

sum = 0
for line in sys.stdin:
    sum += int(line)

print(f"File total {sum}")
