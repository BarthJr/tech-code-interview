"""
>>> word_split('themanran', ['the', 'ran', 'man'])
['the', 'man', 'ran']
>>> word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John'])
['i', 'love', 'dogs', 'John']
>>> word_split('themanran', ['clown', 'ran', 'man'])
[]
"""


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []
    if not phrase:
        return
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output
