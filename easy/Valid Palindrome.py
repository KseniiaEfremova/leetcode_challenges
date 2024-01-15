def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalpha() and not s[left].isnumeric():
            left += 1
        elif not s[right].isalpha() and not s[right].isnumeric():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


assert not isPalindrome("abc")
assert not isPalindrome("abca")
assert not isPalindrome("ab")
assert isPalindrome("aba")
assert isPalindrome("abA")
assert isPalindrome(".Abc  cba")
assert isPalindrome("ab 121 ,.:ba")
