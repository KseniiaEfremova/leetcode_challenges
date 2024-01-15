def isPalindrome(x: int) -> bool:
    # O(len(digits)) time
    # O(len(digits)) space
    if x < 0:
        return False
    first_num = x
    new_num = 0
    while x > 0:
        new_num = new_num*10 + x % 10
        x = x // 10
    return first_num == new_num


assert isPalindrome(121) is True
assert isPalindrome(1001) is True
assert isPalindrome(1) is True
assert isPalindrome(-1) is False
assert isPalindrome(11121) is False
assert isPalindrome(1212) is False


# def isPalindrome(x: int) -> bool:
#     # O(1) time
#     # O(n) space
#     if x < 0:
#         return False
#     x = str(x)
#     return x == x[::-1]