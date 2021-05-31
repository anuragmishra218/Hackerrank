from itertools import product

K, M = 3, 1000
N = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]
results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
print(list(results))
#print(max(results))
