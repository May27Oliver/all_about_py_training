from typing import Dict, List


# Question:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
def two_sum(arr: List[int], target: int) -> List[int]:
    counter: Dict[int, int] = {}
    indx = 0
    for i in arr:
        if i in counter:
            return [counter[i], i]
        else:
            counter[target - i] = i
    return [0]


print(two_sum([1, 2, 3, 4], 4))
