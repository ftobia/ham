import pytest


class TestWord(object):

    def test_str(self):
        from ham import Word
        assert str(Word('foo')) == 'foo'

    def test_repr(self):
        from ham import Word
        assert repr(Word('foo')) == '<Word "foo">'

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


class TestSymbols(object):

    def test(self):
        from ham.symbols import *
        symbols = ['AA', 'AA0', 'AA1', 'AA2', 'AE', 'AE0', 'AE1', 'AE2', 'AH',
            'AH0', 'AH1', 'AH2', 'AO', 'AO0', 'AO1', 'AO2', 'AW', 'AW0', 'AW1',
            'AW2', 'AY', 'AY0', 'AY1', 'AY2', 'B', 'CH', 'D', 'DH', 'EH', 'EH0',
            'EH1', 'EH2', 'ER', 'ER0', 'ER1', 'ER2', 'EY', 'EY0', 'EY1', 'EY2',
            'F', 'G', 'HH', 'IH', 'IH0', 'IH1', 'IH2', 'IY', 'IY0', 'IY1',
            'IY2', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OW0', 'OW1', 'OW2',
            'OY', 'OY0', 'OY1', 'OY2', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH',
            'UH0', 'UH1', 'UH2', 'UW', 'UW0', 'UW1', 'UW2', 'V', 'W', 'Y', 'Z',
            'ZH']
        for symbol in symbols:
            assert symbol in locals()

