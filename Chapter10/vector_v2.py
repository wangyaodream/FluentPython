from array import array
import reprlib
import math
from abc import ABC

class Vector:
    typecode = 'd'

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




    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

if __name__ == '__main__':
    # v1 = Vector([3,4,5])
    # print(len(v1))
    # print(v1[0],v1[-1])
    # v7 = Vector(range(7))
    # print(v7[1:4])
    v7 = Vector(range(7))
    print(v7[1:])
    print(v7[1:4])
