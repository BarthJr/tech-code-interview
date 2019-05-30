"""
>>> lst = ['banana', 'banana', 'abacaxi', 'caqui', ]
>>> dedup(lst)
['banana', 'abacaxi', 'caqui']

"""
from typing import List


def dedup(lst: List) -> List:
    """Remove duplicates from lst, maintaining order"""
    aux = dict()
    for i in lst:
        if i not in aux:
            aux[i] = 1
    return list(aux.keys())
