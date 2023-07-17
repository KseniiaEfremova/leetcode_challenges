def lengthOfLastWord(s: str) -> int:
    count = 0
    for k in range(len(s)-1, -1, -1):
        if not s[k].isspace():
            count += 1
        elif count:
            return count
    return count


assert lengthOfLastWord("qq qq") == 2
assert lengthOfLastWord("qq qq  ") == 2
assert lengthOfLastWord("qqqq") == 4
assert lengthOfLastWord("qq qq") == 2
assert lengthOfLastWord("qq qq") == 2
