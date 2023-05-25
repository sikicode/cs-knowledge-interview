# O(1) insertion, delete, and lookup
# https://wiki.python.org/moin/TimeComplexity
class Set:
    def __init__(self, *args):
        self._dict = {}
        for arg in args:
            self.add(arg)

    def __repr__(self):
        import string
        elems = list(map(repr, self._dict.keys()))
        elems.sort()
        return "%s(%s)" % (self.__class__.__name__, ", ".join(elems))

    def add(self, item):
        self._dict[item] = item

s = Set(1,2)
print(s.__repr__())
