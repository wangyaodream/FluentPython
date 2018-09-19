import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

    '''支持洗牌，添加setitem方法'''
    def __setitem__(self, key, value):
        self._cards[key] = value

    '''继承了MutableSequence抽象类就必须要实现delitem方法'''
    def __delitem__(self, key):
        del self._cards[key]

    def insert(self,pos,value):
        self._cards.insert(pos,value)

