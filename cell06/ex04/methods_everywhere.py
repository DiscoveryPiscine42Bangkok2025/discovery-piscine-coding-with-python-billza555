#!/usr/bin/env python3
import sys
def shrink(text):
    return text[0:8]
def enlarge(text):
    while len(text) < 8:
        text += "Z"
    return text
if len(sys.argv) >= 2:
    words = sys.argv[1:]
    for word in words:
        if(len(word) >= 8):
            print(shrink(word))
        else:
            print(enlarge(word))
else:
    print("none")