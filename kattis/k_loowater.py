'''
Compute minimal amount to match one list against another in >= fashion

Status: Accepted
'''

from bisect import bisect_left

###############################################################################

def main():
    """Read input and print output"""

    while True:
        dragons, knights = [int(i) for i in input().split()]
        if dragons == 0 and knights == 0:
            break

        doomed = dragons > knights
        if doomed:
            for _ in range(dragons + knights):
                input()
        else:
            dsize, ksize = [None] * dragons, [None] * knights
            for i in range(dragons):
                dsize[i] = int(input())
            for i in range(knights):
                ksize[i] = int(input())
            dsize.sort(reverse=True)
            ksize.sort()

            budget = 0
            for dragon in dsize:
                knight_index = bisect_left(ksize, dragon)
                if knight_index == len(ksize):
                    doomed = True
                    break
                budget += ksize[knight_index]
                del ksize[knight_index]

        if doomed:
            print('Loowater is doomed!')
        else:
            print(budget)

###############################################################################

if __name__ == '__main__':
    main()
