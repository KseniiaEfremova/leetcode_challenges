def plusOne(digit: list) -> list:
    for i in range(len(digit) - 1, -1, -1):
        if digit[i] == 9:
            digit[i] = 0
        else:
            digit[i] += 1
            return digit
    digit.append(0)
    digit[0] = 1
    return digit


def plusOne_(digits: list) -> list:
    number = 0
    k = -1
    n = 1
    while k >= -(len(digits)):
        number += digits[k] * n
        n *= 10
        k -= 1
    number += 1
    new_digits = []
    while number > 0:
        new_digits.append(number % 10)
        number = number // 10
    return new_digits[::-1]
