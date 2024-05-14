#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    prev = 0
    for i in roman_string:
        if roman_dict[i] > prev:
            total += roman_dict[i] - 2 * prev
        else:
            total += roman_dict[i]
        prev = roman_dict[i]
    return total
