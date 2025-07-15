#!/usr/bin/env python3
import sys

current_category = None
count = 0

for line in sys.stdin:
    category, value = line.strip().split('\t')
    if current_category == category:
        count += 1
    else:
        if current_category and count > 114:
            print(f"{current_category}\t{count}")
        current_category = category
        count = 1

if current_category and count > 114:
    print(f"{current_category}\t{count}")
