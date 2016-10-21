import random

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for el in items:
            yield el.get(args[0])
    else:
        for el in items:
            a = {}
            for key in args:
                if not el.get(key) is None:
                    a[key] = el[key]
                else:
                    break
            if len(a) != 0:
                yield a

def gen_random(begin, end, num_count):
    pass
    for i in range(num_count):
        yield random.randint(begin, end)
