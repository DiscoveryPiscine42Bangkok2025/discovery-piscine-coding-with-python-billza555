#!/usr/bin/env python3
array_number = [2, 8, 9, 48, 8, 22, -12, 2]
new_array_number = set(x + 2 for x in array_number if x > 5)
print(f"{array_number}")
print(f"{new_array_number}")