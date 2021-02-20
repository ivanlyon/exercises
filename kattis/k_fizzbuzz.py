'''
The interview question

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    fizzing, buzzing, domain = [int(i) for i in input().split()]
    result = [*range(domain + 1)]
    for index in range(domain + 1):
        if index % fizzing == 0:
            result[index] = "Fizz"
    for index in range(domain + 1):
        if index % buzzing == 0:
            if result[index] == "Fizz":
                result[index] = "FizzBuzz"
            else:
                result[index] = "Buzz"

    for line in result[1:]:
        print(line)

###############################################################################

if __name__ == '__main__':
    main()
