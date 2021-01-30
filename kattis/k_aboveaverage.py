'''
Determine percentage of scores above average

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print percentage of above average scores"""

    for _ in range(int(input())):
        grades = [int(i) for i in input().strip().split()][1:]
        average = sum(grades) / len(grades)
        aboves = len([i for i in grades if i > average])
        result = aboves / len(grades)
        print('{0:.3%}'.format(result))

###############################################################################

if __name__ == '__main__':
    main()
