import random 
from tombola import Tombola

class Bingocage(Tombola):
    def __init__(self,items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self,items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()

if __name__ == '__main__':
    l = [1,2,3,4,5]
    tmp = Bingocage(l)
    print(tmp.pick())
    print(tmp._items)
