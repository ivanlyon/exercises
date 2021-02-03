'''
Determine sum of toilet input and render as toilet output

Status: Accepted

LCD bar encoding based on binary flagging of individual segments

  +-0-+
1 |   | 2
  |   |
  +-3-+
4 |   | 5
  |   |
  +-6-+

'''

###############################################################################

def main():
    """Read input and print output score of toilet addition"""

    lcd_bars = {}
    lcd_bars['0'] = [0, 1, 2, 4, 5, 6]
    lcd_bars['1'] = [2, 5]
    lcd_bars['2'] = [0, 2, 3, 4, 6]
    lcd_bars['3'] = [0, 2, 3, 5, 6]
    lcd_bars['4'] = [1, 2, 3, 5]
    lcd_bars['5'] = [0, 1, 3, 5, 6]
    lcd_bars['6'] = [0, 1, 3, 4, 5, 6]
    lcd_bars['7'] = [0, 2, 5]
    lcd_bars['8'] = [0, 1, 2, 3, 4, 5, 6]
    lcd_bars['9'] = [0, 1, 2, 3, 5, 6]
    lcd_bars['+'] = [3]

    lcd_output = []
    text = []
    for _ in range(7):
        text.append(input())
        lcd_output.append('')

    lcd_text = ''
    for lhs in range(0, len(text[0]), 6):
        on_bars = []
        on_bars += [i for i in [0] if text[0][lhs + 1] == 'x']
        on_bars += [i for i in [1] if text[1][lhs + 0] == 'x']
        on_bars += [i for i in [2] if text[2][lhs + 4] == 'x']
        on_bars += [i for i in [3] if text[3][lhs + 2] == 'x']
        on_bars += [i for i in [4] if text[4][lhs + 0] == 'x']
        on_bars += [i for i in [5] if text[5][lhs + 4] == 'x']
        on_bars += [i for i in [6] if text[6][lhs + 2] == 'x']
        for value in lcd_bars:
            if lcd_bars[value] == on_bars:
                lcd_text += value

    result = sum([int(i) for i in lcd_text.split('+')])
    first_digit = True
    while result or first_digit:
        last_digit = result % 10
        matrix = [list('.....') for _ in range(7)]

        for segment in lcd_bars[str(last_digit)]:
            if segment in (0, 3, 6):
                for i in range(5):
                    matrix[segment][i] = 'x'
            elif segment in (1, 4):
                for i in range(4):
                    matrix[segment - 1 + i][0] = 'x'
            elif segment in (2, 5):
                for i in range(4):
                    matrix[segment - 2 + i][4] = 'x'
            else:
                assert False

        if first_digit:
            for line in range(7):
                lcd_output[line] = ''.join(matrix[line])
        else:
            for line in range(7):
                lcd_output[line] = ''.join(matrix[line]) + '.' + lcd_output[line]
        first_digit = False
        result //= 10

    for line in range(7):
        print(lcd_output[line])

###############################################################################

if __name__ == '__main__':
    main()
