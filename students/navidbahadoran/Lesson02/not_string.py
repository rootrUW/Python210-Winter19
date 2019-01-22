"""
title: not_string
change log:
NBahadoran, 1/19/2018, Created not_string.py
"""
def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the front.
    However, if the string already begins with "not", return the string unchanged.
    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
    """
    if "not".lower() in str[0:3]:
        return str
    return "not "+str

print(not_string("hello"))

