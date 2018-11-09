import sys
class Mapping:
    def __init__(self, iterable):
        self.items = []
        self._update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items.append(item)
    _update = update
class SubMapping(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items.append(item)
    def show(self):
        print self.items
values = [{"a":"b", "C":"D"}]
submapping = SubMapping(values)
keys = [1, 2, 3]
values = ["a", "b", "c"]
submapping.update(keys, values)
submapping.show()
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print "B"
    except C:
        print "C"
    except D:
        print "D"
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse("spam")
for char in rev:
    print char
