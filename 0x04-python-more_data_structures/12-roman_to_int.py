#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert roman numeral to integer
    Return integer
    """
    if (
            roman_string is None or
            type(roman_string) is not str or
            len(roman_string) == 0 or
            " " in roman_string
            ):
        return 0
    roman_symbols = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
            }
    ro_to_int = 0
    prev_symbol = roman_string[0]
    for symbol in roman_string:
        if roman_symbols[prev_symbol] < roman_symbols[symbol]:
            ro_to_int -= roman_symbols[prev_symbol]
            ro_to_int += roman_symbols[prev_symbol + symbol]
        else:
            ro_to_int += roman_symbols[symbol]
        prev_symbol = symbol
    return ro_to_int
