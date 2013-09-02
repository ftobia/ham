from ._version import __version__
from .symbols import *

FILL_CHAR = '.'


class Word(object):

    def __init__(self, word):
        self._letters = list(word)

    def __str__(self):
        return ''.join(self._letters)

    def __repr__(self):
        return '<Word "{0!s}">'.format(self)

    def __iter__(self):
        return iter(self._letters)

    def __eq__(self, other):
        return (type(self) is type(other) and
                self._letters == other._letters)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __contains__(self, obj):
        return obj in str(self)

    def __len__(self):
        return len(str(self).replace(FILL_CHAR, ''))

    def pop(self, seq):
        if seq not in self:
            raise ValueError('"{0!s}" is not in word'.format(seq))
        index = str(self).find(seq)
        s = slice(index, index + len(seq))
        chunk = self._letters[s]
        self._letters[s] = FILL_CHAR * len(seq)
        return ''.join(chunk)

    def vowel_groups(self):
        vowels = 'aeiouy'
        word = str(self)
        acc = []
        for letter in word:
            if letter in vowels:
                acc.append(letter)
            else:
                if acc:
                    yield ''.join(acc)
                    acc = []
        if acc:
            yield ''.join(acc)


class Pronunciation(object):

    def __init__(self, phonemes):
        self._phonemes = list(phonemes)

    def __contains__(self, obj):
        try:
            last_item = obj[-1]
        except TypeError:
            return False
        if last_item in '012':
            return obj in self._phonemes
        else:
            for phoneme in self._phonemes:
                if obj in phoneme:
                    return True
            return False

    def __str__(self):
        return ' '.join(self._phonemes)

    def __repr__(self):
        return '<Pronunciation "{0}">'.format(str(self))

    def __iter__(self):
        return iter(self._phonemes)

    def __len__(self):
        return len(self._phonemes)

    def __eq__(self, other):
        return (type(self) is type(other) and
                self._phonemes == other._phonemes)

    def __ne__(self, other):
        return not self.__eq__(other)

    def index(self, value, start=0):
        for i, phoneme in enumerate(self._phonemes):
            if i < start:
                continue
            if value in phoneme:
                return i
        raise ValueError("'{0!s}' is not in pronunciation".format(value))


class SoundPairing(object):

    def __init__(self, word, pronunciation):
        self.word = Word(word)
        self.pronunciation = Pronunciation(pronunciation)
        self.phonograms = [''] * len(self.pronunciation)
