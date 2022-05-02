# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
def palindrome(num: int) -> bool:
    compare_num = 0
    pointer = num
    while pointer > 0:
        n = pointer % 10
        pointer = pointer // 10
        compare_num = compare_num * 10 + n
    return compare_num == num


print(palindrome(121))
