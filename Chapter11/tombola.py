import abc

class Tombola(abc.ABC):
    '''创建抽象方法'''
    @abc.abstractmethod
    def load(self,iterable):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
            如果实例为空，抛出错误
        """

    def loaded(self):
        '''如果至少有一个元素，返回TRUE 否则返回FALSE'''
        return bool(self.inspect())

    def inspect(self):
        '''返回一个有序元组'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            self.load(items)
            return tuple(sorted(items))