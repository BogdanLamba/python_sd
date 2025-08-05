
#1. **Built-in Types**:
x: int = 10
name: str = "Python"
price: float = 99.99
is_valid: bool = True

#2. **Collections with Their Types**:
from typing import List, Dict, Set, Tuple

numbers: List[int] = [1, 2, 3]
pairs: Dict[str, int] = {"a": 1, "b": 2}
unique_items: Set[str] = {"apple", "banana"}
coordinates: Tuple[int, int] = (10, 20)

#3. **Optional and Union Types**:
from typing import Optional, Union

# Can be string or None
name: Optional[str] = None  # Same as Union[str, None]

# Can be either int or str
id_number: Union[int, str] = "ABC123"

# 4. Custom classes
class User:
    pass

def get_user() -> User:
    return User()

# 5.  **Type Aliases**:
from typing import List, Dict

# Creating type aliases
from typing import List, Dict

Vector = List[float]
Points = Dict[str, Tuple[int, int]]

def scale(v: Vector) -> Vector:
    return [x * 2 for x in v]

# 6. Callable types:
from typing import Callable

def apply(func: Callable[[int], str], value: int) -> str:
    return func(value)

# 7. **Literal Types**
from typing import Literal

# Valid values can only be "red", "green", or "blue"
color: Literal["red", "green", "blue"] = "red"

# Valid values can only be 1, 2, or 3
dice_roll: Literal[1, 2, 3] = 2

# 8.  **Generic Types**:
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, item: T):
        self.item: T = item

int_box: Box[int] = Box(123)
str_box: Box[str] = Box("hello")

#9. **Protocol Types** (Python 3.8+):
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()
