"""
Ham is a toolkit for manipulating words, pronunciations, and phonemes.

.. testsetup::

    from ham import Pronunciation, Word
"""
from ._version import __version__
from .symbols import *

FILL_CHAR = '.'


class NLTKModuleNotFound(Exception):
    pass


class CMUDictCache(object):
    _has_nltk = None
    _cmudict = None

    @property
    def has_nltk(self):
        if self._has_nltk is None:
            try:
                import nltk
            except ImportError:
                self._has_nltk = False
            else:
                self._has_nltk = True
        return self._has_nltk

    @property
    def cmudict(self):
        if not self.has_nltk:
            raise NLTKModuleNotFound
        if self._cmudict is None:
            import nltk.corpus
            self._cmudict = nltk.corpus.cmudict.dict()
        return self._cmudict

cache = CMUDictCache()


class Word(object):
    """
    Encapsulates a word.
    """

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
        """
        Return and remove a letter or sequence of letters.

        .. doctest::

            >>> hello = Word('hello')
            >>> hello.pop('el')
            'el'
            >>> str(hello)
            'h..lo'

        If seq does not exist, raise a ValueError.
        """
        if seq not in self:
            raise ValueError('"{0!s}" is not in word'.format(seq))
        index = str(self).find(seq)
        s = slice(index, index + len(seq))
        chunk = self._letters[s]
        self._letters[s] = FILL_CHAR * len(seq)
        return ''.join(chunk)

    def vowel_groups(self):
        """
        Generator that yields consecutive groups of vowels.

        .. doctest::

            >>> list(Word('onomatopoeia').vowel_groups())
            ['o', 'o', 'a', 'o', 'oeia']
        """
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

    def pronunciations(self):
        """
        Returns a list of Pronunciations for the word.

        Looks the word up in the CMU pronouncing dictionary
        (http://www.speech.cs.cmu.edu/cgi-bin/cmudict)

        If the word does not exist in the pronouncing dictionary,
        return an empty list.

        .. doctest::

            >>> Word('hungry').pronunciations()
            [<Pronunciation "HH AH1 NG G R IY0">]
            >>> Word('chewbacca').pronunciations()
            []
        """
        try:
            pronunciations = cache.cmudict[str(self)]
        except KeyError:
            return []
        return [Pronunciation(p) for p in pronunciations]


class Pronunciation(object):
    """
    A wrapper around a list of phonemes.
    """

    def __init__(self, phonemes):
        self._phonemes = list(phonemes)

    def __contains__(self, obj):
        """
        Checks if a phoneme is in this pronunciation.

        If the phoneme is an unstressed vowel, that phoneme will be compared
        against contained vowels without regard to stress. Otherwise, if the
        phoneme is a stressed vowel sound, the stress will be taken into
        account.

        .. doctest::

            >>> 'AA' in Pronunciation(['B', 'AA1', 'R', 'N'])
            True

            >>> 'AW0' in Pronunciation(['B', 'R', 'AW1', 'N'])
            False
        """
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
        """
        Return the first index of value, starting at the start index given.

        If an unstressed vowel is given, will return the first index with that
        vowel sound regardless of stress. Otherwise index will only find a
        vowel sound with identical stress.

        .. doctest::

            >>> Pronunciation(['B', 'AA1', 'R', 'N']).index('AA')
            1
        """
        for i, phoneme in enumerate(self._phonemes):
            if i < start:
                continue
            if value in phoneme:
                return i
        raise ValueError("'{0!s}' is not in pronunciation".format(value))


class SoundPairing(object):
    """
    A SoundPairing is for mapping a word with a pronunciation. It is used as an
    intermediate step for breaking a word into its phonograms.
    """

    def __init__(self, word, pronunciation):
        self.word = Word(word)
        self.pronunciation = Pronunciation(pronunciation)
        self.phonograms = [''] * len(self.pronunciation)
