def is_valid(s):
    if not s:
        return False

    stack_round = []
    stack_square = []
    stack_bracket = []

    for char in s:
        if char == "(":
            stack_round.append(char)
        elif char == "[":
            stack_square.append(char)
        elif char == "{":
            stack_bracket.append(char)

        else:
            if char == ")":
                if not stack_round:
                    return False
                else:
                    stack_round.pop()
            elif char == "]":
                if not stack_square:
                    return False
                else:
                    stack_square.pop()
            elif char == "}":
                if not stack_bracket:
                    return False
                else:
                    stack_bracket.pop()

    if not stack_round and not stack_square and not stack_bracket:
        return True

    return False


s1 = "(]"
s2 = "}{}"
s3 = "][]"
s4 = ")"
s5 = "{}"
s6 = "[()]"
s7 = "((()"
s8 = ")((("
s9 = "[]))))"
s10 = "([)]"

print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s3))
print(is_valid(s4))
print(is_valid(s5))
print(is_valid(s6))
print(is_valid(s7))
print(is_valid(s8))
print(is_valid(s9))
print(is_valid(s10))
