# Ensures hierarchy among parentheses is obeyed.
# If there is a nested expressions, the bracket squares must be the outmots element,
# followed by square brackets and then round brackets.


def is_valid(s):

    stack = []
    parentheses_dictionary = {")": "(", "]": "[", "}": "{"}
    parentheses_levels = {"{": 3, "[": 2, "(": 1}

    for i, char in enumerate(s):
        if char in parentheses_dictionary.values():
            if not stack or parentheses_levels[char] <= parentheses_levels[stack[-1]]:
                stack.append(char)
                if (
                    len(stack) > 1
                    and parentheses_levels[stack[-1]] - parentheses_levels[stack[-2]]
                    > 1
                ):
                    return False
            else:
                return False
        else:
            if not stack:
                return False
            else:
                if (
                    char in parentheses_dictionary
                    and stack[-1] == parentheses_dictionary[char]
                ):
                    stack.pop()
                else:
                    return False
    if not stack:
        print(
            "debug",
            stack,
            parentheses_levels[stack[-1]],
            parentheses_levels[stack[-2]],
        )
        return True
    return False


# s1 = "(])"
# s2 = "}{}"
# s3 = "[]"
# s4 = ")"
# s5 = "[](){}"
# s6 = "[()]"
# s7 = "((()"
# s8 = ")((("
# s9 = "[](){}"
# s10 = "({})"
# s11 = "{[()]}"
# s12 = "(){}()()()()[]"
# s13 = "{[(())]}"
s14 = "{[]()()}"  # must be False
# s15 = "[]((()))(){}"
# s16 = "{[]((()))}"  # must be False
# s17 = "{((()))}"  # must be False

input_list = [
    # s1,
    # s2,
    # s3,
    # s4,
    # s5,
    # s6,
    # s7,
    # s8,
    # s9,
    # s10,
    # s11,
    # s12,
    # s13,
    s14,
    # s15,
    # s16,
    # s17,
]

for i, input_string in enumerate(input_list):
    print(i + 1, is_valid(input_string))
