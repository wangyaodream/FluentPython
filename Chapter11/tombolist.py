from random import randrange

from tombola import Tombola

@Tombola.register  #这里是利用注册成为Tombola的虚拟子类
class Tombolist(list):
    #这里继承了list  是list类的真实子类
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty Tombolist')

    load = list.extend #list.entend是list类，将Tombola.load抽象方法指向list类的方法

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

    