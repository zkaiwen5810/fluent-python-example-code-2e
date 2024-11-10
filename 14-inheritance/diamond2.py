from diamond import A

class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()
    
class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()

class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() in LeafAU')
        super().ping()

if __name__ == '__main__':
    leaf2 = LeafUA()
    leaf2.ping()

    print(f'{LeafUA} __mro__: ', LeafUA.__mro__)

    leaf3 = LeafAU()
    leaf3.ping()
    print(f'{LeafAU} __mro__: ', LeafAU.__mro__)