'''
Determine fate of 3 personnel approaching 2 enemies.

Status: Accepted
'''

###############################################################################

def how_many_attack(dogs, arrival_time):
    '''Return text number of dogs who attack visitor at arrival_time.'''

    result = 0
    dog1time = arrival_time % (dogs[0] + dogs[1])
    if dog1time in range(1, dogs[0] + 1):
        result += 1

    dog2time = arrival_time % (dogs[2] + dogs[3])
    if dog2time in range(1, dogs[2] + 1):
        result += 1

    return ["none", "one", "both"][result]

###############################################################################

if __name__ == '__main__':
    DOGS = [int(i) for i in input().split()]
    for person in [int(i) for i in input().split()]:
        print(how_many_attack(DOGS, person))

###############################################################################
