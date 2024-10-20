import random
from tombola import Tombola

@Tombola.register
class Tombolist(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pick from empty Tombolist')
    
    load = list.extend

    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(self)

if __name__ == '__main__':
    print(issubclass(Tombolist, Tombola))
    t = Tombolist(range(100))
    print(isinstance(t, Tombola))
    print(Tombolist.__mro__)