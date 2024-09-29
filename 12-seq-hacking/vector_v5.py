from array import array
import functools
import itertools
import math
import operator
import reprlib


class Vector:
    typecode = 'd'
    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes(ord(self.typecode)) + 
                bytes(self._components))
    
    def __eq__(self, other: object) -> bool:
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    
    def __hash__(self) -> int:
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]
    
    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)
    
    def __setattr__(self, name: str, value) -> None:
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(attr_name=name, cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(name, value)
    
    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
    
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())

            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(','.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
if __name__ == '__main__':
    v7 = Vector(range(7))
    print(v7[1:4])
    print(v7[-1:])

    v8 = Vector(range(7))
    print(v7 == v8)

    print(format(v7, '.3eh'))
    print(format(v7, '.3e'))
    