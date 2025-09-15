#!/usr/bin/env python3
import sys
if len(sys.argv) == 3:
    least = int(sys.argv[1])
    most = int(sys.argv[2])
    array_number = []
    while least <= most:
        array_number.append(least)
        least += 1
    print(array_number)
else:
    print("none")