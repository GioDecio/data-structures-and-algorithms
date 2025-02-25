"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


inputs = {
    "ama": "Exp: True",
    "race a car": "Exp: False",
    "A man, a plan, a canal: Panama": "Exp: True",
    "pimperepettenusa": "Exp: False",
}

for input in inputs:
    print(f"{inputs[input]} - R: {is_palindrome(input)}")
