'''
Determine largest sum of 4 numbers.

Status: Accepted
'''

###############################################################################

def main():
    """Output owner of largest dice sum expected result"""

    gunn_dice_sum = sum(map(int, input().strip().split()))
    emma_dice_sum = sum(map(int, input().strip().split()))
    if gunn_dice_sum > emma_dice_sum:
        print("Gunnar")
    elif gunn_dice_sum < emma_dice_sum:
        print("Emma")
    else:
        print("Tie")

###############################################################################

if __name__ == '__main__':
    main()
