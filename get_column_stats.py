import sys
import math
import argparse as ap


def parse():  # parses arguments
    parser = ap.ArgumentParser()

    parser.add_argument('-i',
                        '--filen',
                        type=str,
                        required=True)

    parser.add_argument('-c',
                        '--colnum',
                        type=int,
                        required=True)

    return parser.parse_args()


def stringcheck(V):
    return isinstance(V, int)


def getmean(V):
    if (len(V) == 0):
        return None
    else:
        mean = sum(V)/len(V)
        return mean


def getsd(V, mean):
    if (len(V) == 0):
        return None
    sd = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    return sd


def main():
    args = parse()
    filename = args.filen
    col_num = args.colnum - 1  # since column starts at 0
    mean = 0
    stdev = 0

    V = []  # create vector
    try:
        file = open(args.filen, 'r')  # open file, with check
    except Exception:
        print('file open error')
        sys.exit(1)

    if col_num < 1:  # column number check, with error message
        print('invalid column #')
        sys.exit(1)

    for l in file:
        A = [int(x) for x in l.split()]  # reads in
        try:
            V.append(A[col_num])
            stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
        finally:
            mean = sum(V)/len(V)
            stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == "__main__":
    main()
