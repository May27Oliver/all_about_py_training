
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List
import unittest


def findCommonPrefix(arr: List[str]) -> str:
    keyStr = arr[0]
    tmpStr = ""
    for s in keyStr:
        tmpStr += s
        for i in range(1, len(arr)):
            if arr[i].find(tmpStr) != 0:
                if len(tmpStr) > 1:
                    return tmpStr[:i]
                else:
                    return ""
    return tmpStr


class FindCommonPrefixTest(unittest.TestCase):
    def test_findCommonPrefix(self):
        self.assertEqual(findCommonPrefix(["flower", "flow", "flight"]), "fl")


if __name__ == '__main__':
    unittest.main()
