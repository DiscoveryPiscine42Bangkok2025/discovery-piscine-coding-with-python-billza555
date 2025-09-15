#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
for i in range(3):
    year = (i+1) * 10
    print(f"In {year} years, you'll be {age+year} years old.")