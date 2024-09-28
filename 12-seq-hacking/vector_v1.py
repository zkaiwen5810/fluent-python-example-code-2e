from array import array
import math
import reprlib


class Vector:
    typecode = 'd'

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
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(*self)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __len__(self):
        return len(self._components)
    
    def __getitem__(self, index):
        return self._components[index]
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)