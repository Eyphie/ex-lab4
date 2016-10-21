# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items) if isinstance(items, list) else items
        self.ignore_case = kwargs.get("ignore_case", False)
        self.lst = []
        pass

    def __next__(self):
        while True:
            el = next(self.items)
            if self.ignore_case:
                if self.lst.count(el.lower()) == 0:
                    self.lst.append(el.lower())
                    return el
                else:
                    continue
            else:
                if self.lst.count(el) == 0:
                    self.lst.append(el)
                    return el
                else:
                    continue
        raise StopIteration

    def __iter__(self):
        return self


