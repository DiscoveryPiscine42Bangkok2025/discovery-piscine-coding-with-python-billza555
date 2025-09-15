#!/usr/bin/env python3
import sys
if len(sys.argv) == 2:
    search = sys.argv[1]
    word = input()
    if search in word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")