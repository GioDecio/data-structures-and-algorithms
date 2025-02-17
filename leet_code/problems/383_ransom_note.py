"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""


def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    d = {}

    for char in magazine:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for char in ransomNote:
        if char in d and d[char] > 0:
            d[char] -= 1
        else:
            return False

    return True
