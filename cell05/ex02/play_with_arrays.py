#!/usr/bin/env python3
array_number = [2, 8, 9, 48, 8, 22, -12, 2]
new_array_number = [x + 2 for x in array_number if x > 5]
print(f"Original array: {array_number}")
print(f"New array: {new_array_number}")