import pytest

from ham import Pronunciation


class TestPronunciation(object):

    def test_constructor(self):
        ink = Pronunciation(['IH1', 'NG', 'K'])
        ink2 = Pronunciation(ink)
        assert ink == ink2
        assert ink is not ink2

    def test_str(self):
        assert str(Pronunciation(['HH', 'AO1', 'NG', 'K'])) == 'HH AO1 NG K'

    def test_repr(self):
        assert repr(Pronunciation(['M', 'AH1', 'NG', 'K', 'IY0'])) == \
            '<Pronunciation "M AH1 NG K IY0">'

    def test_iter(self):
        phonemes = ['G', 'L', 'AE1', 'S']
        pronunciation = Pronunciation(phonemes)
        i = iter(pronunciation)
        assert list(i) == phonemes
        with pytest.raises(StopIteration):
            next(i)
        assert list(pronunciation) == phonemes

    def test_contains(self):
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
        word = Pronunciation(['W', 'ER1', 'D'])
        assert None not in word
        assert word not in word

    def test_eq(self):
        hello = Pronunciation(['HH', 'AH0', 'L', 'OW1'])
        assert hello == hello
        assert hello == Pronunciation(hello)
        assert hello == Pronunciation(['HH', 'AH0', 'L', 'OW1'])
        assert not (hello == Pronunciation(['G', 'UH2', 'D', 'B', 'AY1']))

    def test_ne(self):
        assert Pronunciation(['HH', 'AH0', 'L', 'OW1']) != \
            Pronunciation(['G', 'UH2', 'D', 'B', 'AY1'])
        assert Pronunciation(['HH', 'AH0', 'L', 'OW1']) != \
            ['HH', 'AH0', 'L', 'OW1']
        assert not (Pronunciation(['HH', 'AH0', 'L', 'OW1']) !=
                    Pronunciation(['HH', 'AH0', 'L', 'OW1']))

    def test_len(self):
        assert len(Pronunciation(['AH0'])) == 1
        assert len(Pronunciation(['HH', 'AY1'])) == 2
        assert len(Pronunciation(['G', 'L', 'OW1'])) == 3
        assert len(Pronunciation(['K', 'L', 'IH1', 'P'])) == 4

    def test_index(self):
        p = Pronunciation(['M', 'IH2', 'S', 'IH0', 'S', 'IH1', 'P', 'IY0'])
        assert p.index('M') == 0
        assert p.index('S') == 2
        assert p.index('S', 1) == 2
        assert p.index('S', 2) == 2
        assert p.index('S', 3) == 4
        assert p.index('S', 4) == 4
        with pytest.raises(ValueError) as excinfo1:
            p.index('S', 5)
        assert str(excinfo1.value) == "'S' is not in pronunciation"
        with pytest.raises(ValueError) as excinfo2:
            p.index('K')
        assert str(excinfo2.value) == "'K' is not in pronunciation"
        assert p.index('IH2') == 1
        with pytest.raises(ValueError) as excinfo3:
            p.index('IH2', 2)
        assert str(excinfo3.value) == "'IH2' is not in pronunciation"
        assert p.index('IH0') == 3
        with pytest.raises(ValueError) as excinfo4:
            p.index('IH0', 4)
        assert str(excinfo4.value) == "'IH0' is not in pronunciation"
        assert p.index('IH1') == 5
        with pytest.raises(ValueError) as excinfo5:
            p.index('IH1', 6)
        assert str(excinfo5.value) == "'IH1' is not in pronunciation"
        assert p.index('IH') == 1
        assert p.index('IH', 2) == 3
        assert p.index('IH', 4) == 5
        with pytest.raises(ValueError) as excinfo6:
            p.index('IH', 6)
        assert str(excinfo6.value) == "'IH' is not in pronunciation"
