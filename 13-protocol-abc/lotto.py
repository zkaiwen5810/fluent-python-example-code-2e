import random
from tombola import Tombola

class LottoBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)
    
    def load(self, iterable):
        self._balls.extend(iterable)
    
    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(position)
    
    def loaded(self):
        return bool(self._balls)
    
    def inpsect(self):
        return tuple(self._balls)