def isPalindrome(x: int) -> bool:
    # O(1) time
    # O(n) space
    if x < 0:
        return False
    x = str(x)
    return x[::] == x[::-1]


assert isPalindrome(121) == True
assert isPalindrome(11) == True
assert isPalindrome(1) == True
assert isPalindrome(-1) == False
assert isPalindrome(11121) == False
assert isPalindrome(1212) == False
