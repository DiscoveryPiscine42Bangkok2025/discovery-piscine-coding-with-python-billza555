#!/usr/bin/env python3
import sys
if len(sys.argv) >= 3:
    words = list(reversed(sys.argv[1:]))
    for w in words:
        print(w)
else:
    print("none")
