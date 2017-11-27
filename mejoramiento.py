import argparse
from random import choice
from dataset import BANCOS, DIST, MAX_CAMION, MONTO


def _check_solution(solution):
    if not all(s in BANCOS for s in solution):
        raise argparse.ArgumentTypeError("Solution must contain all banks")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--solution', required=True)
    parser.add_argument('-k', type=int, default=1)

    args = parser.parse_args()
    _check_solution(args.solution)
    return args


def show_current(solution):
    print "The current solution is {}, with a score of {}".format(solution, calc_solution(solution))


def swap(l, a, b):
    l[b], l[a] = l[a], l[b]


def is_solution(solution):
    """
    Checks whether or not the solution is possible
    """
    truck = MONTO['O']
    for node in solution:
        truck += MONTO[node]
        if (truck < 0) or (truck > MAX_CAMION):
            return False
    return True

def permutate(solution, k):
    new_solution = list(solution)  # Make a copy
    current_score = calc_solution(solution)
    for i in range(k):
        a = choice(range(len(solution)))
        b = choice(range(len(solution)))
        swap(new_solution, a, b)
        print "Trying with: {}".format(new_solution)
        if is_solution(new_solution) and calc_solution(new_solution) > current_score:
            show_current(new_solution)
        else:
            permutate(solution, k)



def calc_solution(solution):
    """
    Returns the value of a given solution
    """
    counter = 0
    _index = 0
    for node in solution:
        index = BANCOS.index(node) + 1  # The first element is the root
        dist = DIST[_index, index]
        #print "Node: {}, dist: {}".format(node, dist)
        counter += dist
        _index = index
    counter += DIST[_index, 0]  # Going back to the root
    return counter


def main():
    args = parse_args()
    show_current(args.solution)
    permutate(**vars(args))


if __name__ == '__main__':
    main()
