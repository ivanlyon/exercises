"""
hexdec.py services a unittest tutorial on top of custom functions to convert
integers to and from string representations of hexadecimal values.

Reference: http://www.bogotobogo.com/python/python_unit_testing.php

Input:
------
    The first line contains a single integer for the number of test cases.
Each test case then appears on its own line as a word ('hex2dec' or 'dec2hex')
and a value to be converted.
  +------------------------------------------------------------------+
  | 2                                                                |
  | toHex(1024)                                                      |
  | toDec(1F4)                                                       |
  +------------------------------------------------------------------+

Output:
-------
    For each test case, the result will displayed on a line.
  +------------------------------------------------------------------+
  | toHex(1024) = 400                                                |
  | toDec(1F4) = 500                                                 |
  +------------------------------------------------------------------+
"""

class NotIntegerError(ValueError): pass
class NotHexadecimalError(ValueError): pass

HEXADECIMAL_VALUES = list("0123456789ABCDEF")

###############################################################################

def toHex(d):
    """convert string of decimal to string of hexadecimal"""
    from string import digits

    value = 0
    for c in d:
        if c in digits:
            value = value * 10 + int(c)
        else:
            raise NotIntegerError('input must be non-negative integer')

    result = ''
    if value:
        while value:
            result += HEXADECIMAL_VALUES[value % 16]
            value //= 16
    else:
        result = '0'

    return result[::-1]

###############################################################################

def toDec(h):
    """convert string of hexadecimal to string of decimal"""
    BASE10_VALUE = {}
    BASE10_VALUE['0'] = 0
    BASE10_VALUE['1'] = 1
    BASE10_VALUE['2'] = 2
    BASE10_VALUE['3'] = 3
    BASE10_VALUE['4'] = 4
    BASE10_VALUE['5'] = 5
    BASE10_VALUE['6'] = 6
    BASE10_VALUE['7'] = 7
    BASE10_VALUE['8'] = 8
    BASE10_VALUE['9'] = 9
    BASE10_VALUE['A'] = 10
    BASE10_VALUE['B'] = 11
    BASE10_VALUE['C'] = 12
    BASE10_VALUE['D'] = 13
    BASE10_VALUE['E'] = 14
    BASE10_VALUE['F'] = 15

    result = 0
    for c in h.upper():
        if c in HEXADECIMAL_VALUES:
            result = result * 16 + BASE10_VALUE[c]
        else:
            raise NotHexadecimalError('input must be non-negative hexadecimal')

    return str(result)

###############################################################################

if __name__ == '__main__':
    for testCases in range(int(input().strip())):
        text = input().strip()
        lparen = text.find('(')
        rparen = text.rfind(')')
        command = text[:lparen]
        value = text[lparen + 1: rparen]
        if command == 'toDec':
            print(text + ' = ' + toDec(value))
        elif command == 'toHex':
            print(text + ' = ' + toHex(value))
        else:
            print("Invalid command detected:", command)
