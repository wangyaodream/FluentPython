from collections import abc

class FrozenJSON:

    def __init__(self,mapping): #确保传入的是一个字典，并且为了安全创建副本
        self.__data = dict(mapping)

    def __getattr__(self, name): #仅当没有指定名称的属性时才调用
        if hasattr(self.__data,name):
            return getattr(self.__data,name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls,obj):
        if isinstance(obj,abc.Mapping):
            return cls(obj)
        elif isinstance(obj,abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__=="__main__":
    grad = FrozenJSON({'name':'wangyao','age':18})
    print(grad.age)
    obj = FrozenJSON({'name':'zhangman','age':28,'Idol':['wql','self']})
    print(obj.Idol)