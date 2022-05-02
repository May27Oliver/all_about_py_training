# Given a roman numeral, convert it to an integer.
from json.encoder import INFINITY
from typing import Dict


def roman_to_int(roman: str) -> float:
    roman_dict: Dict[str, float] = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    sum: float = 0
    last_s = INFINITY
    for s in roman:
        if roman_dict[s]:
            tmp = roman_dict[s]
            if last_s < tmp:
                sum += tmp - last_s * 2
            else:
                sum += tmp
            last_s = tmp
    return sum


print(roman_to_int("MDCLV"))
