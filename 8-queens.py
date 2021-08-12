import copy
from typing import List


def permutation(a: List) -> List:
    if len(a) == 1:
        return [a]
    perm = []
    for i in a:
        b = copy.copy(a)
        b.remove(i)
        for p in permutation(b):
            perm.append([i] + p)
    return perm


valid_sols = []
d1 = [1, 2, 3]
for sol in permutation(d1):
    sum1 = set()
    sum2 = set()
    for i in range(3):
        sum1.add(sol[i] + i)
        sum2.add(sol[i] + 4 - i)
    if len(sum1) == 3 and len(sum2) == 3:
        valid_sols.append(sol)

print(valid_sols)
print(len(valid_sols))
