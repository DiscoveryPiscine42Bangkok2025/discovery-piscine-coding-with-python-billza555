#!/usr/bin/env python3
def find_the_redheads(dict):
    return [k for k, v in dict.items() if v == "red"]
    
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
