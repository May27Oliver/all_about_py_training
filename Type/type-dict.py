from typing import TypedDict

# TypedDict是為了在Dict中要除存異質資料的情況準備的，比方JSON,API


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float
