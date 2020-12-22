"""
Minimal number of given intervals necessary to span arbitrary interval

Status: Accepted
"""

import sys
from collections import namedtuple

Span = namedtuple('Span', ['lhs', 'rhs', 'idx'])

###############################################################################

def solver(numbers, is_demo=False):
    """Solve all test cases of interval cover formatted input"""
    total_size = len(numbers)
    index = 0

    while index < total_size:
        cover_a, cover_b = numbers[index], numbers[index + 1]
        index += 3 # +1 for next integer

        interval = []
        for span_num in range(int(numbers[index - 1])):
            interval.append(Span(numbers[index], numbers[index + 1], span_num))
            index += 2

        minimal = []
        sorts = sorted(interval)
        input_lo = sorts[0].lhs
        input_hi = max([num.rhs for num in interval])
        if input_lo <= cover_a and cover_b <= input_hi:
            left_span = cover_a
            max_rhs = sorts[0]
            for candidate in sorts:
                if candidate.lhs <= left_span:
                    if candidate.rhs > max_rhs.rhs:
                        max_rhs = candidate
                else:
                    if candidate.lhs <= max_rhs.rhs:
                        minimal.append(max_rhs.idx)
                        left_span = max_rhs.rhs
                        max_rhs = candidate
                    else:
                        minimal = []
                        break
                if max_rhs.rhs >= cover_b:
                    minimal.append(max_rhs.idx)
                    break

        if is_demo:
            return minimal
        if minimal:
            print(str(len(minimal)))
            print(' '.join([str(result) for result in minimal]))
        else:
            print("impossible")

###############################################################################

def main():
    """Read input for solver()"""

    numbers = []
    for i in sys.stdin.read().splitlines():
        numbers += [float(k) for k in i.split()]
    solver(numbers, is_demo=False)

###############################################################################

def demo():
    '''Interval cover demonstration with random spans'''
    import matplotlib.pyplot as plt
    import random

    span = []
    cover_lhs = 10
    cover_rhs = 90
    numbers = [cover_lhs, cover_rhs]
    spans = random.randint(14, 24)
    numbers.append(spans)
    for _ in range(spans):
        lhs = random.random() * 100.0
        rhs = lhs + random.random() * 40.0
        numbers.append(lhs)
        numbers.append(rhs)
        span.append([numbers[-2], numbers[-1]])
        print(str(len(span) - 1) + ': ' + str(span[-1]))

    print()
    results = solver(numbers, is_demo=True)
    if results:
        print("Interval " + str(cover_lhs) + "-" + str(cover_rhs) + " covered by spans:")
        for res in results:
            print(str(res))
    else:
        print("impossible")

    fig, axes = plt.subplots()
    plt.suptitle('Interval Cover Demonstration (' + str(spans) + ' random spans)')
    axes.set_xlabel('Span Values')
    axes.set_ylabel('Span Index')
    axes.set_xlim(-5, 105)
    axes.set_ylim(-1, 1 + spans)
    if results:
        axes.title.set_text('Minimal # of intervals to cover {:d} to {:d} is {:d} spans'.format(cover_lhs, cover_rhs, len(results)))
        fig.set_facecolor('#eeffee')
    else:
        axes.title.set_text('Intervals to cover {:d} to {:d} is impossible'.format(cover_lhs, cover_rhs))
        fig.set_facecolor('#ffdddd')
    axes.plot([cover_lhs, cover_lhs], [-5, 1+spans], color='red')
    axes.plot([cover_rhs, cover_rhs], [-5, 1+spans], color='red')
    for line in range(spans):
        ylevel = [line, line]
        if line in results:
            axes.plot(span[line], ylevel, marker='D', linewidth=1, color='green')
        else:
            axes.plot(span[line], ylevel, marker='o', linewidth=1, color='blue')
    plt.show()

###############################################################################

if __name__ == '__main__':
    import argparse
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("--demo", help="interval cover demonstration", action="store_true")
    ARGS = PARSER.parse_args()
    if ARGS.demo:
        demo()
    else:
        main()
