from array import array
import math

class Vector2d:
    __match_args__ = ('x', 'y')

    typecode = 'd'

    def __init__(self, x, y) -> None:
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)
    
    def __format__(self, format_spec: str) -> str:
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)
    
    @classmethod
    def frombytes(cls, octests):
        typecode = chr(octests[0])
        memv = memoryview(octests[1:]).cast(typecode)
        return cls(*memv)
    
if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1)
    print()

    octets = bytes(v1)
    print(octets)
    print()

    print(abs(v1))
    print()

    v1_clone = Vector2d.frombytes(bytes(v1))
    print(v1)
    print(v1 == v1_clone)
    print()

    print(format(v1, '.2f'))
    print(format(v1, '.3e'))
    print(format(v1, '.3ep'))
    print()

    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(len({v1, v2}))
    print()