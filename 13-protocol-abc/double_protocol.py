from typing import Protocol, TypeVar


T = TypeVar('T')

class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T: ...

RT = TypeVar('RT', bound=Repeatable)

def double(x: Repeatable) -> RT:
    return x * 2