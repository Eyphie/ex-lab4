#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
print(sys.getdefaultencoding())

path = sys.argv[1]

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding="cp1251") as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(unique([i for i in field(arg, 'job-name')], ignore_case=True), key=lambda x: x.lower())

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('Программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    sal = list(gen_random(100000, 200000, len(arg)))
    return list('{}, зарплата {} руб.'.format(r, sal) for r, sal in zip(arg, sal))

with timer():
    f4(f3(f2(f1(data))))
