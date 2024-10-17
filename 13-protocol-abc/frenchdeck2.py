
from collections import abc, namedtuple


Card = namedtuple('Card', ['rank', 'suit'])

class FrenchCard2(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def __getitem__(self, position: int) -> Card:
        return self._cards[position]
    
    def __setitem__(self, position: int, value: Card):
        self._cards[position] = value

    def __delitem__(self, position: int):
        del self._cards[position]
    
    def insert(self, position: int, value: Card):
        self._cards.insert(position, value)

if __name__ == '__main__':
    french_card = FrenchCard2()
    print('construct success')