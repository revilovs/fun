"""
This is a small script to simulate the following situation, which might be the starting point for various different
games:
A group of n people each write their name on a piece of paper and put that snippet in a hat.
That hat is then passed around and everyone draws a snippet from the hat. Whenever someone draws their own snippet,
he puts it back into hat and draws a different one. If the last person to draw a snippet draws their own one, all
snippets are put back into the hat and the drawing starts again.

Once all snippets are distributed, one could draw a (directed) graph, connecting each person to the one whose snippet
they have drawn. The question that now arises is: Does this resulting graph form a Hamiltonian cycle, i.e. a cycle that
visits each node/person exactly once (as opposed to multiple smaller cycles being created)? Or rather, how big is the
probability for this?
"""
import random
from collections import Counter
from typing import List


def get_initial_result_and_hat(n: int):
    return [], [i for i in range(n)]


def pass_around_hat(n: int):
    result, hat = get_initial_result_and_hat(n)

    while len(hat):
        snippet = random.choice(hat)

        if snippet == len(result):
            if len(result) == n - 1:
                result, hat = get_initial_result_and_hat(n)
        else:
            hat.remove(snippet)
            result.append(snippet)

    return result


def is_hamiltonian(draw: List[int]):
    index = 0
    result = []

    while draw[index] not in result:
        result.append(draw[index])
        index = draw[index]

    return len(draw) == len(result)


def estimate(n: int, k: int):
    return sum(is_hamiltonian(pass_around_hat(n)) for _ in range(k)) / k


def print_estimations(n_min, n_max, k):
    for n in range(n_min, n_max):
        print(f"n={n}, p={estimate(n, k)}")


def print_draw_stats(n, k):
    counter = Counter(str(pass_around_hat(n)) for _ in range(k))

    for (draw, count) in counter.most_common():
        print(f'{draw}, {is_hamiltonian(eval(draw))}, {count}, {count / k}')

    print(f'Number of different draws: {len(counter)}')


def main():
    k = 1000000
    n_min = 4
    n_max = 10
    n = 3

    print_estimations(n_min, n_max, k)

    print_draw_stats(n, k)


if __name__ == '__main__':
    main()
