'''
String matching with tolerance

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    stored, password = input(), input()
    accepted = False
    if len(stored) == len(password) + 1:
        if stored.startswith(password):
            accepted = stored[-1].isdigit()
        elif stored.endswith(password):
            accepted = stored[0].isdigit()
    else:
        accepted = (stored == password) or (stored == password.swapcase())

    if accepted:
        print("Yes")
    else:
        print("No")

###############################################################################

if __name__ == '__main__':
    main()
