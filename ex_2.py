#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2
first = Unique(data1)
for i in first:
    if i is None:
        continue
    else:
        print(i, end=' ')
print()


second = Unique(list(data2))
for i in second:
    if i is None:
        continue
    else:
        print(i, end=' ')
print()


third = Unique(data3)
for i in third:
    if i is None:
        continue
    else:
        print(i, end=' ')
print()

fourth = Unique(data3, ignore_case=1)
for i in fourth:
    if i is None:
        continue
    else:
        print(i, end=' ')
print()
