#!/usr/bin/env python3
result = ""
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) != 'q' and chr(letter) != 'e':
        result += chr(letter)
print(result)
