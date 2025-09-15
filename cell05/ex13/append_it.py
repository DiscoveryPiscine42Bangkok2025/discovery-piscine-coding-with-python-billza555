#!/usr/bin/env python3
import sys
if len(sys.argv) >= 3:
    words = sys.argv[1:]
    for i in range(len(words)):
        if(i % 2 == 0):
            print(words[i] + "ism")
else:
    print("none")
