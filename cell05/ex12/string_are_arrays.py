#!/usr/bin/env python3
import sys
if len(sys.argv) == 2:
    words = sys.argv[1]
    count = words.count("z")
    if count > 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")