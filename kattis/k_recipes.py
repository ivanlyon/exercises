'''
Scale numbers by ratio

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    for test_case in range(1, 1 + int(input().strip())):
        print('Recipe #', test_case)
        ingreds, written, needed = [int(i) for i in input().split()]
        ratio = needed / written
        ingred = {}
        for _ in range(ingreds):
            name, weight, percent = input().split()
            ingred[name] = (float(weight), float(percent))
            if percent == '100.0':
                weight100 = float(weight)
        for i in ingred:
            weight, percent = ingred[i]
            print(i + ' {0:.1f}'.format(weight100 * ratio * percent / 100.0))
        print('----------------------------------------')

###############################################################################

if __name__ == '__main__':
    main()
