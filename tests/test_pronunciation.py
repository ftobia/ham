import pytest


class TestPronunciation(object):

    def test_constructor(self):
        from ham import Pronunciation
        ink = Pronunciation(['IH1', 'NG', 'K'])
        ink2 = Pronunciation(ink)
        assert ink == ink2
        assert ink is not ink2

    def test_str(self):
        from ham import Pronunciation
        assert str(Pronunciation(['HH', 'AO1', 'NG', 'K'])) == 'HH AO1 NG K'

    def test_repr(self):
        from ham import Pronunciation
        assert repr(Pronunciation(['M', 'AH1', 'NG', 'K', 'IY0'])) == \
            '<Pronunciation "M AH1 NG K IY0">'

    def test_iter(self):
        from ham import Pronunciation
        phonemes = ['G', 'L', 'AE1', 'S']
        pronunciation = Pronunciation(phonemes)
        i = iter(pronunciation)
        assert list(i) == phonemes
        with pytest.raises(StopIteration):
            next(i)
        assert list(pronunciation) == phonemes

    def test_contains(self):
        from ham import Pronunciation
        from ham.symbols import AH, AH0, AH1, AH2, IY, IY0, IY1, IY2
        monkey = Pronunciation(['M', 'AH1', 'NG', 'K', 'IY0'])
        assert AH in monkey
        assert AH0 not in monkey
        assert AH1 in monkey
        assert AH2 not in monkey
        assert IY in monkey
        assert IY0 in monkey
        assert IY1 not in monkey
        assert IY2 not in monkey

    def test_contains_incorrect_types(self):
        from ham import Pronunciation
        word = Pronunciation(['W', 'ER1', 'D'])
        assert None not in word
        assert word not in word

    def test_eq(self):
        from ham import Pronunciation
        hello = Pronunciation(['HH', 'AH0', 'L', 'OW1'])
        assert hello == hello
        assert hello == Pronunciation(hello)
        assert hello == Pronunciation(['HH', 'AH0', 'L', 'OW1'])
        assert not (hello == Pronunciation(['G', 'UH2', 'D', 'B', 'AY1']))

    def test_ne(self):
        from ham import Pronunciation
        assert Pronunciation(['HH', 'AH0', 'L', 'OW1']) != \
            Pronunciation(['G', 'UH2', 'D', 'B', 'AY1'])
        assert Pronunciation(['HH', 'AH0', 'L', 'OW1']) != \
            ['HH', 'AH0', 'L', 'OW1']
        assert not (Pronunciation(['HH', 'AH0', 'L', 'OW1']) !=
                    Pronunciation(['HH', 'AH0', 'L', 'OW1']))

    def test_len(self):
        from ham import Pronunciation
        assert len(Pronunciation(['AH0'])) == 1
        assert len(Pronunciation(['HH', 'AY1'])) == 2
        assert len(Pronunciation(['G', 'L', 'OW1'])) == 3
        assert len(Pronunciation(['K', 'L', 'IH1', 'P'])) == 4
