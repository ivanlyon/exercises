'''
Determine both scores of a programming contest team

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output score of programming contest team"""

    solved = set()
    scored = {}
    while True:
        log_entry = input().strip()
        if log_entry.startswith('-1'):
            break

        minutes, problem, result = log_entry.split()

        if not problem in solved:
            if not problem in scored:
                scored[problem] = 0

            if result == 'right':
                solved.add(problem)
                scored[problem] += int(minutes)
            else:
                scored[problem] += 20

    print(len(solved), sum([scored[i] for i in solved]))

###############################################################################

if __name__ == '__main__':
    main()
