'''
Score of points plotted on scoring circles

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    target = [0]
    for i in range(20, 220, 20):
        target.append(i * i)

    for _ in range(int(input())):
        result = 0
        for _points in range(int(input())):
            x, y = map(int, input().split())
            distance2 = x * x + y * y
            if distance2 <= 40000:
                for score in range(1, 11):
                    if target[score] >= distance2:
                        result += 11 - score
                        break
        print(result)

###############################################################################

if __name__ == '__main__':
    main()
