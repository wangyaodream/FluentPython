from array import array
import reprlib
import math
import functools # reduce
import operator # xor (异或)


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self,components):
        self._components = array(self.typecode,components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        #return str(tuple(self))
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    #支持可切片
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index,slice):
            return cls(self._components[index])
        elif isinstance(index,int):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))


    #针对属性动态添加
    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in self.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(attr_name=key,cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(key,value)


    #实现hash散列 之前的__eq__是必要方法之一
    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor,hashes,0)


    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)