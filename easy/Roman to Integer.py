def romanToInt(s: str) -> int:
    # O(n) time
    # O(1) space
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            return res + roman[s[i]]
        if roman[s[i]] >= roman[s[i+1]]:
            res += roman[s[i]]
            i += 1
        else:
            res += roman[s[i+1]] - roman[s[i]]
            i += 2
    return res


assert romanToInt("III") == 3
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994
assert romanToInt("M") == 1000
assert romanToInt("IV") == 4
assert romanToInt("I") == 1
assert romanToInt("I") == 1

