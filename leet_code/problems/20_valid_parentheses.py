def is_valid(s):

    stack = []
    for char in s:
        if char == "(":
            stack.append(char)

    if not stack:
        return False

    for char in s:
        if char != "(":
            stack.pop()
        if len(stack) == 0:
            return True
        # print(stack, len(stack))
    return False


s1 = "((()))"
s2 = ")))))"
s3 = "((((("
s4 = ")"
s5 = ""

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
print(is_valid(s5))
