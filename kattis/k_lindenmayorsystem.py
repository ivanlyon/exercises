'''
Determine result of linden mayor rules given start string and iterations

Status: Accepted
'''

###############################################################################

def lindenmayor(rule, evolutions, start):
    
    text = start
    for _ in range(evolutions):
        temp = []
        for letter in list(text):
            if letter in rule:
                temp.append(rule[letter])
            else:
                temp.append(letter)
        text = ''.join(temp)

    return text

###############################################################################

def main():
    """Read input and print output for sum of digits between 2 numbers"""

    rules, evolutions = [int(i) for i in input().strip().split()]

    rule = {}
    for _ in range(rules):
        start, finish = input().strip().split(' -> ')
        rule[start] = finish

    print(lindenmayor(rule, evolutions, input().strip()))

###############################################################################

def demo():
    import random

    rule = {}
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = ''.join(random.sample(letters, random.randint(10, 15)))
    print("Given the start text: " + text)
    print("And the sequence modification rules:")

    rules = random.sample(letters, random.randint(6, 10))
    for letter in rules:
        rule[letter] = ''.join(random.sample(letters, random.randint(1, 4)))
        print(letter + ' -> ' + rule[letter])
    print('The text changes for each iteration in the following fashion:')
    print('0 ' + text)

    for index in range(1, 10):
        iteration = lindenmayor(rule, 1, text)
        if len(iteration) >= 80:
            print('...')
            break
        print(str(index) + ' ' + iteration)
        if iteration == text:
            break
        text = iteration
    
###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="linden mayor system", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
