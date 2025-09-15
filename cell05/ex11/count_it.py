#!/usr/bin/env python3
import sys
if len(sys.argv) >= 2:
    words = sys.argv[1:]
    print(f"parameters: {len(words)}")
    for word in words:
        print(f"{word}: {len(word)}")
else:
    print("none")