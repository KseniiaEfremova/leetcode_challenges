def longestCommonPrefix(strs: list) -> str:
    for prefix_len in range(len(strs[0])):
        letter = strs[0][prefix_len]
        common = True
        for s in strs:
            if prefix_len >= len(s) or s[prefix_len] != letter:
                common = False
                break
        if not common:
            return strs[0][:prefix_len]
    return strs[0]


assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
assert longestCommonPrefix(["afl","afl","afli"]) == "afl"
assert longestCommonPrefix(["flowe","fl","f"]) == "f"
assert longestCommonPrefix(["a","a","b"]) == ""
assert longestCommonPrefix(["","","b"]) == ""

