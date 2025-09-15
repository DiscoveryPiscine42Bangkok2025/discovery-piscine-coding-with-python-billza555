#!/usr/bin/env python3
import sys
def downcase_it(text):
    return text.lower()
if len(sys.argv) >= 2:
    words = sys.argv[1:]
    for word in words:
        print(downcase_it(word))
else:
    print("none")