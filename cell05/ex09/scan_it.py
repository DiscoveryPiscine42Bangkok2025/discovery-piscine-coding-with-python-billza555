#!/usr/bin/env python3
import sys
if len(sys.argv) == 3:
    search = sys.argv[1]
    word = sys.argv[2]
    count = word.count(search)
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")