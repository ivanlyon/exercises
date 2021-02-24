'''
Precompute equations of fixed operations and number.

Status: Accepted
'''

###############################################################################

def eval2(text):
    """Evaluate an expression without using eval()"""

    numbers, operators = [], []
    for glyph in text.split():
        if glyph.isdigit():
            rhs = int(glyph)
            if operators and operators[-1] in '*/':
                lhs = numbers.pop()
                operating = operators.pop()
                if operating == '*':
                    numbers.append(lhs * rhs)
                else:
                    numbers.append(lhs // rhs)
            else:
                numbers.append(rhs)
        else:
            operators.append(glyph)

    while operators:
        lhs, rhs = numbers[0], numbers[1]
        operating = operators[0]
        if operating == '+':
            numbers = [lhs + rhs] + numbers[2:]
        else:
            numbers = [lhs - rhs] + numbers[2:]
        operators = operators[1:]

    return numbers.pop()

###############################################################################

def main():
    """Read input and print output"""

    precomp = {}
    for op1 in '+-*/':
        for op3 in '+-*/':
            for op5 in '+-*/':
                text = '4 ' + ' 4 '.join([op1, op3, op5]) + ' 4'
                precomp[eval2(text)] = text

    for _ in range(int(input())):
        number = int(input())
        if number in precomp:
            print(precomp[number], '=', number)
        else:
            print('no solution')

###############################################################################

if __name__ == '__main__':
    main()
