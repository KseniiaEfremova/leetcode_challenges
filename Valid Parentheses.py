def isValid(s: str) -> bool:
    if s[0] == ")" or s[0] == "}" or s[0] == "]":
        return False
    last_char = []
    for el in s:
        if el == "(" or el == "{" or el == "[":
            last_char.append(el)
        else:
            if len(last_char) == 0:
                return False
            if el == ")":
                if last_char[-1] == "(":
                    last_char.pop()
                else:
                    return False
            elif el == "}":
                if last_char[-1] == "{":
                    last_char.pop()
                else:
                    return False
            else:
                if last_char[-1] == "[":
                    last_char.pop()
                else:
                    return False
    return len(last_char) == 0


assert isValid("()")
assert isValid("{}")
assert isValid("[]")
assert isValid("()[]{}")
assert isValid("([{()}])")
assert not isValid(")")
assert not isValid("(")
assert not isValid("([{)])")
assert not isValid("([{()})")
assert not isValid("(){}}{")