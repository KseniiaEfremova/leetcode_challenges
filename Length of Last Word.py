def lengthOfLastWord(s: str) -> int:
    list_words = s.split()
    return len(list_words[-1])
