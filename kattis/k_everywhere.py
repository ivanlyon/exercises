'''
Compute # of unique labels.

Status: Accepted
'''

###############################################################################

def uniques(inputs):
    '''Compute # of unique labels in a list'''

    return len(set(inputs))

###############################################################################

if __name__ == '__main__':
    testcases = int(input())
    for t in range(testcases):
        worktrips = int(input())
        destinations = []
        for w in range(worktrips):
            destinations.append(input())
        print(uniques(destinations))

###############################################################################
