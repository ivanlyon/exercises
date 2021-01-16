'''
Determine sum of integer digits between two inclusive limits

Status: Accepted
'''

###############################################################################

def digit_sum(value):
    """Return the sum of all digits between 0 and input value"""

    result = 0
    if value > 0:
        magnitude = value // 10
        magnitude_sum = sum([int(i) for i in list(str(magnitude))])

        result = digit_sum(magnitude - 1) * 10
        result += 45 * magnitude
        for last_digit in range(1 + value % 10):
            result += magnitude_sum + last_digit

    return result

###############################################################################

def main():
    """Read input and print output for sum of digits between 2 numbers"""

    for _ in range(int(input().strip())):
        lo_value, hi_value = [int(i) for i in input().split()]
        if hi_value:
            if lo_value:
                print(str(digit_sum(hi_value) - digit_sum(lo_value - 1)))
            else:
                print(str(digit_sum(hi_value)))
        else:
            print('0')

###############################################################################

if __name__ == '__main__':
    main()
