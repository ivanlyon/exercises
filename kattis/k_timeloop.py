'''
Print number of lines where number is read from stdin.

Status: Accepted
'''

###############################################################################

def createOutput(times):
    result = []
    for i in range(times):
        result.append(str(i + 1) + ' Abradabra')
    return result

###############################################################################

if __name__ == '__main__':
    for r in createOutput(int(input())):
        print(r)

###############################################################################
