import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""
    
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise 'LookupError' when the instance is empty.
        """
    
    def loaded(self):
        """Return 'True' if there's at least 1 item, 'False' otherwise"""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                item = self.pick()
                items.append(item)
            except LookupError:
                break
        self.load(items)
        return tuple(items)

if __name__ == '__main__':
    class Fake(Tombola):
        def pick(self):
            return 13
    
    Fake
    f = Fake()