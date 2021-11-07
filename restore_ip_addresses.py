# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s.
# You can return them in any order.
#
# A valid IP address consists of exactly four integers,
# each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example,
# "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1"
# are invalid IP addresses.

"""
>>> restoreIpAddresses('1921680')
['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0']
>>> restoreIpAddresses('25525511135')
['255.255.11.135', '255.255.111.35']
>>> restoreIpAddresses('0000')
['0.0.0.0']
"""


# O(1) time | O(1) space
def restoreIpAddresses(string):
    output = []
    MAX = len(string)
    MAX_PART_LENGTH = 4
    partial_ip = [''] * MAX_PART_LENGTH
    end = lambda a: min(a + MAX_PART_LENGTH, MAX)

    for i in range(1, end(0)):
        partial_ip[0] = string[:i]
        if not isValid(partial_ip[0]):
            continue
        for j in range(i + 1, end(i)):
            partial_ip[1] = string[i:j]
            if not isValid(partial_ip[1]):
                continue
            for k in range(j + 1, end(j)):
                partial_ip[2] = string[j:k]
                if not isValid(partial_ip[2]):
                    continue
                partial_ip[3] = string[k:]
                if not isValid(partial_ip[3]):
                    continue
                output.append('.'.join(partial_ip))

    return output


def isValid(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))
