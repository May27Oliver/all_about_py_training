from typing import List
import unittest


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid_idx = len(arr) // 2
    left_arr = merge_sort(arr[:mid_idx])
    right_arr = merge_sort(arr[mid_idx:])

    return merge(left_arr, right_arr)


def merge(left: List[int], right: List[int]) -> List[int]:
    final, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    while i < len(left):
        final.append(left[i])
        i += 1
    while j < len(right):
        final.append(right[j])
        j += 1
    return final


class FindCommonPrefixTest(unittest.TestCase):
    def test_findCommonPrefix(self):
        self.assertEqual(merge_sort([4, 7, 1, 2, 5, 3, 8, 10, 33, 6, 77, 100, 101]), [
                         1, 2, 3, 4, 5, 6, 7, 8, 10, 33, 77, 100, 101])


if __name__ == '__main__':
    unittest.main()
