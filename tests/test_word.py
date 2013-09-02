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
        assert str(excinfo.value) == '"a" is not in word'

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

    def test_vowel_groups(self):
        from ham import Word
        assert list(Word('hello').vowel_groups()) == ['e', 'o']
        assert list(Word('monkey').vowel_groups()) == ['o', 'ey']
        assert list(Word('toast').vowel_groups()) == ['oa']
        assert list(Word('abomination').vowel_groups()) == \
            ['a', 'o', 'i', 'a', 'io']
        assert list(Word('unceremoniously').vowel_groups()) == \
            ['u', 'e', 'e', 'o', 'iou', 'y']
