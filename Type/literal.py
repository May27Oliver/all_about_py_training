from dataclasses import dataclass
from typing import Literal, Set

# Literal可以限制回傳值的內容


@dataclass
class Error:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burgur"]
    condiments: Set[Literal["Mustard", "Ketchup"]]


Error(0, False)
# error: Argument 1 to "Error" has incompatible type "Literal[0]"; expected "Literal[1, 2, 3, 4, 5]"
Snack("Invalid", set())
# error: Argument 1 to "Snack" has incompatible type "Literal['Invalid']"; expected "Literal['Pretzel', 'Hot Dog', 'Veggie Burgur']"
Snack("Pretzel", {"Mustard", "Relish"})
# error: Argument 2 to <set> has incompatible type "Literal['Relish']"; expected "Literal['Mustard', 'Ketchup']"
