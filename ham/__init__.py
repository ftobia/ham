from ._version import __version__

FILL_CHAR = '.'


class Word(object):

    def __init__(self, word):
        self._letters = list(word)

    def __str__(self):
        return ''.join(self._letters)

    def __repr__(self):
        return '<Word "{!s}">'.format(self)

    def __contains__(self, obj):
        return obj in str(self)

    def __len__(self):
        return len(str(self).replace(FILL_CHAR, ''))

    def pop(self, seq):
        if seq not in self:
            raise ValueError('"{!s}" is not in word'.format(seq))
        index = str(self).find(seq)
        s = slice(index, index + len(seq))
        chunk = self._letters[s]
        self._letters[s] = FILL_CHAR * len(seq)
        return ''.join(chunk)
