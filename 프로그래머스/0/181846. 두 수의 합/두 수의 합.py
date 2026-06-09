def solution(a, b):
    carry = 0
    result = ""

    while a or b or carry:
        x = int(a[-1]) if a else 0
        y = int(b[-1]) if b else 0

        s = x + y + carry
        result = str(s % 10) + result
        carry = s // 10

        a = a[:-1]
        b = b[:-1]

    return result