def strStr(haystack: str, needle: str) -> int:
    i = 0
    k = 0
    while k < len(haystack):
        if haystack[k] == needle[i]:
            i += 1
        else:
            if i > 0:
                k = k - i
            i = 0
        k += 1
        if i == len(needle):
            return k - i
    return -1


assert strStr("sadbutsad", "sad") == 0
assert strStr("sadbutsad", "but") == 3
assert strStr("sadbutsad", "sadq") == -1
assert strStr("sadbutsad", "wer") == -1
assert strStr("sabutsad", "ad") == 6
assert strStr("mississippi", "issip") == 4
assert strStr("mississippi", "pi") == 9
