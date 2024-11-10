class Root:
    def ping(self):
        print(f'{self}.ping() in Root')
    
    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self) -> str:
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()
    
    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()
    
    def pong(self):
        print(f'{self}.pong() in B')

class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()

if __name__ == '__main__':
    leaf1 = Leaf()
    leaf1.ping()
    leaf1.pong()

    print(f'{Leaf} __mro__: ', Leaf.__mro__)