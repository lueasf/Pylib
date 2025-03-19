import itertools as it
### Practice with itertools

elements = ['a', 'b', 'c']
combinations = list(it.combinations(elements, 2))
# combinations = [('a', 'b'), ('a', 'c'), ('b', 'c')]

permutations = list(it.permutations(elements, 2))
# permutations = [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
permutations = list(it.permutations(elements, 3))
# permutations = [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')] 

l1 = [1, 2]
l2 = [4, 5]
cartesian = list(it.product(l1, l2))
# cartesian = [(1, 4), (1, 5), (2, 4), (2, 5)]

l1 = [1, 2, 3]
cum = list(it.accumulate(l1))
# cum = [1, 3, 6]

from functools import reduce
### Practice with Lambda functions
f = lambda x: x**2
# f(2) = 4
g = lambda x, y: x + y
# g(2, 3) = 5

nb = [1, 2, 3, 4, 5]
sq = list(map(lambda x: x % 2 == 0, nb))
# sq = [2, 4]

nb = [1, 2, 3, 4, 5]
tot = reduce(lambda x, y: x + y, nb)
# reduce calculate the cumulative sum of the list
# tot = 15
