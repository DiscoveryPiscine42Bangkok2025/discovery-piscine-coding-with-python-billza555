#!/usr/bin/env python3
def add_one(x):
    x += 1
    print("Inside add_one:", x) 
number = 5
print("Before add_one:", number)
add_one(number)
print("After add_one:", number)
