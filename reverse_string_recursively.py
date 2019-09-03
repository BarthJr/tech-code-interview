"""
>>> reverse('hello')
'olleh'
>>> reverse('hello world')
'dlrow olleh'
>>> reverse('123456789')
'987654321'
"""


def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
