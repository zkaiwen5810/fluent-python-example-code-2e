
from typing import Any, Protocol, runtime_checkable

@runtime_checkable
class RandomPicker(Protocol):
    def pick(self) -> Any: ...