from itertools import product

K, M = 3, 1000
N = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]

from itertools import product

possible_combination = set(list(product(*N)))
print(possible_combination)
def func(nums):
    return sum(x * x for x in nums) % M


print(max(list(map(func, possible_combination))))