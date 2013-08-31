import pytest


class TestWord(object):

    def test_constructor(self):
        from ham import Word
        slap = Word('slap')
        slap2 = Word(slap)
        assert slap == slap2
        assert slap is not slap2

    def test_str(self):
        from ham import Word
        assert str(Word('foo')) == 'foo'

    def test_repr(self):
        from ham import Word
        assert repr(Word('foo')) == '<Word "foo">'

    def test_iter(self):
        from ham import Word
        word = Word('hello')
        i = iter(word)
        assert ''.join(i) == 'hello'
        with pytest.raises(StopIteration):
            next(i)
        assert ''.join(word) == 'hello'

    def test_contains(self):
        from ham import Word
        foo = Word('foo')
        assert 'f' in foo
        assert 'o' in foo
        assert 'fo' in foo
        assert 'oo' in foo
        assert 'foo' in foo
        assert 'b' not in foo
        assert 'of' not in foo
        assert 'foof' not in foo

    def test_eq(self):
        from ham import Word
        foo = Word('foo')
        assert foo == foo
        assert foo == Word('foo')
        assert foo == Word(foo)
        assert not (foo == Word('monkey'))

    def test_ne(self):
        from ham import Word
        assert Word('monkey') != Word('butler')
        assert Word('monkey') != 'monkey'
        assert not (Word('monkey') != Word('monkey'))

    def test_pop(self):
        from ham import Word
        w = Word('foo')
        assert w.pop('f') == 'f'
        assert str(w) == '.oo'
        assert w.pop('o') == 'o'
        assert str(w) == '..o'
        assert w.pop('o') == 'o'
        assert str(w) == '...'

    def test_pop_nonexistent(self):
        from ham import Word
        w = Word('foo')
        with pytest.raises(ValueError) as excinfo:
            w.pop('a')
        assert excinfo.value.message == '"a" is not in word'

    def test_pop_single_letter_from_middle_of_word(self):
        from ham import Word
        w = Word('primary')
        assert w.pop('m') == 'm'
        assert str(w) == 'pri.ary'

    def test_pop_multiple_letters(self):
        from ham import Word
        w = Word('monkey')
        assert w.pop('onk') == 'onk'
        assert str(w) == 'm...ey'

    def test_len(self):
        from ham import Word
        key = 'key'
        assert len(Word(key)) == len(key)
        monkey = 'monkey'
        assert len(Word(monkey)) == len(monkey)
        w = Word(monkey)
        w.pop(key)
        assert len(w) == len(monkey) - len(key)


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

    # def test_eq(self):
    #     from ham import Word
    #     foo = Word('foo')
    #     assert foo == foo
    #     assert foo == Word('foo')
    #     assert not (foo == Word('monkey'))

    # def test_ne(self):
    #     from ham import Word
    #     assert Word('monkey') != Word('butler')
    #     assert Word('monkey') != 'monkey'
    #     assert not (Word('monkey') != Word('monkey'))

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


class TestSoundPairing(object):

    def test_constructor(self):
        from ham import Word, Pronunciation, SoundPairing
        color = 'color'
        k_ah1_l_er0 = ['K', 'AH1', 'L', 'ER0']
        word = Word(color)
        pronunciation = Pronunciation(k_ah1_l_er0)
        p1 = SoundPairing(word=color, pronunciation=k_ah1_l_er0)
        p2 = SoundPairing(word=color, pronunciation=pronunciation)
        p3 = SoundPairing(word=word, pronunciation=k_ah1_l_er0)
        p4 = SoundPairing(word=word, pronunciation=pronunciation)
        for pairing in [p1, p2, p3, p4]:
            assert pairing.word == Word(color)
            assert pairing.word is not word
            assert pairing.pronunciation == Pronunciation(k_ah1_l_er0)
            assert pairing.pronunciation is not pronunciation


class TestSymbols(object):

    def test(self):
        from ham.symbols import *
        symbols = ['AA', 'AA0', 'AA1', 'AA2', 'AE', 'AE0', 'AE1', 'AE2', 'AH',
                   'AH0', 'AH1', 'AH2', 'AO', 'AO0', 'AO1', 'AO2', 'AW', 'AW0',
                   'AW1', 'AW2', 'AY', 'AY0', 'AY1', 'AY2', 'B', 'CH', 'D',
                   'DH', 'EH', 'EH0', 'EH1', 'EH2', 'ER', 'ER0', 'ER1', 'ER2',
                   'EY', 'EY0', 'EY1', 'EY2', 'F', 'G', 'HH', 'IH', 'IH0',
                   'IH1', 'IH2', 'IY', 'IY0', 'IY1', 'IY2', 'JH', 'K', 'L',
                   'M', 'N', 'NG', 'OW', 'OW0', 'OW1', 'OW2', 'OY', 'OY0',
                   'OY1', 'OY2', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UH0',
                   'UH1', 'UH2', 'UW', 'UW0', 'UW1', 'UW2', 'V', 'W', 'Y', 'Z',
                   'ZH']
        for symbol in symbols:
            assert symbol in locals()
