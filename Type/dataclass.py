from dataclasses import dataclass


from Type.dataclass import dataclass

from typing import Set, Union, Optional

# Union


@dataclass
class Error:
    error_code: int
    disposed_of: bool


@dataclass
class Snack:
    name: str
    condiments: Set[str]


snack: Union[Snack, Error] = Snack("Hotdog", {"Mustard", "Ketchup"})

snack = Error(5, True)

# Optional
# Optional tell developer the value might be None
