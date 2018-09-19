import abc

class Tombola(abc.ABC): #自定义的抽象基类要继承自abc
    
    @abc.abstractmethod
    def load(self,iterbale):
        """从可迭代对象中添加元素"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，则raise LookupError错误"""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
