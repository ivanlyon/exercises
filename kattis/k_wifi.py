'''
Binary search floating point value to tolerance of 0.1

Status: Accepted
'''

###############################################################################

def minmax(covers, value_list):
    '''Return minimum distance from any relocatable cover to covered value.
    Coverage of all points required.  Scheme is to count number of covers
    required to cover the values for a given distance.  If the number of covers
    required exceeds the number of covers specified, then the guess is too
    small, otherwise the guess is too large.'''

    sorted_values = sorted(value_list)
    lo = 0.0
    hi = sorted_values[-1]
    values = len(value_list)

    while (hi - lo) > 0.01:
        mid = (hi + lo) * 0.5
        covered = 0
        used_extra_cover = False
        for cover in range(1, covers + 2):
            # cover_origin = sorted_values[covered] + mid
            cover_limit = sorted_values[covered] + mid + mid
            while covered < values and sorted_values[covered] <= cover_limit:
                covered += 1

            if covered == values:
                break

        if cover == covers + 1:
            lo = mid
        else:
            hi = mid

    return (hi + lo) * .5

###############################################################################

if __name__ == '__main__':
    for testcase in range(int(input())):
        access_points, houses = [int(i) for i in input().split()]
        distances = []
        for _ in range(houses):
            distances += [int(input())]
        print('{:.1f}'.format(minmax(access_points, distances)))

###############################################################################
