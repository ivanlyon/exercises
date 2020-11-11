'''
Determine fate of 3 personnel approaching 2 enemies.

Status: Accepted
'''

###############################################################################

def how_many_attack(dogs, arrival_time):
    '''Return text number of dogs who attack visitor at arrival_time.'''

    result = 0
    dog1time = arrival_time % (dogs[0] + dogs[1])
    if dog1time > 0 and dog1time <= dogs[0]:
        result += 1

    dog2time = arrival_time % (dogs[2] + dogs[3])
    if dog2time > 0 and dog2time <= dogs[2]:
        result += 1

    return ["none", "one", "both"][result]

###############################################################################

if __name__ == '__main__':
    dogs = [int(i) for i in input().split()]
    for person in [int(i) for i in input().split()]:
        print(how_many_attack(dogs, person))

###############################################################################
