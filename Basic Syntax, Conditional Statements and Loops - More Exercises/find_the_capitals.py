word = input()


def getindices(s):
    return [i for i, c in enumerate(s) if c.isupper()]


print(getindices(word))
