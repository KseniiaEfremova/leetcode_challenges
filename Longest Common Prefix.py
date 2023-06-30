def find_the_shortest_word(word_list: list) -> int:
    # O(n) - time complexity
    # O(1) - space complexity
    min_len = len(word_list[0])
    for word in word_list:
        min_len = min(len(word), min_len)
    return min_len


def longestCommonPrefix(strs: list) -> str:
    # O(n**2) - time complexity
    # O(len(longest_pref)) - space complexity
    longest_pref = []
    min_len = find_the_shortest_word(strs)
    for prefix_index in range(min_len):
        letter = strs[0][prefix_index]
        common = True
        for word_index in range(len(strs)):
            if strs[word_index][prefix_index] != letter:
                common = False
                break
        if common:
            longest_pref.append(letter)
        else:
            return ''.join(longest_pref)
    return ''.join(longest_pref)


assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix(["dog","racecar","car"]) == ""
assert longestCommonPrefix(["afl","afl","afli"]) == "afl"
assert longestCommonPrefix(["flowe","fl","f"]) == "f"
assert longestCommonPrefix(["a","a","b"]) == ""
assert longestCommonPrefix(["","","b"]) == ""

