'''
Create a game rank from a win-loss record

Status: Accepted
'''

###############################################################################

def main():
    """Read input and print output"""

    rank_stars = [5] * 11 + [4] * 5 + [3] * 5 + [2] * 5
    rank, stars, last3 = 25, 0, ''
    for game in input():
        if rank:
            last3 = (last3 + game)[-3:]
            if game == 'W':
                stars += 1
                if rank > 5 and last3 == 'WWW':
                    stars += 1
                if stars > rank_stars[rank]:
                    stars -= rank_stars[rank]
                    rank -= 1
            elif rank < 20 or (rank == 20 and stars):
                stars -= 1
                if stars < 0:
                    rank += 1
                    stars = rank_stars[rank] - 1

    if rank:
        print(rank)
    else:
        print('Legend')

###############################################################################

if __name__ == '__main__':
    main()
