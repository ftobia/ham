import pytest

from ham import Word


class TestWord(object):

    def test_constructor(self):
        slap = Word('slap')
        slap2 = Word(slap)
        assert slap == slap2
        assert slap is not slap2

    def test_str(self):
        assert str(Word('foo')) == 'foo'

    def test_repr(self):
        assert repr(Word('foo')) == '<Word "foo">'

    def test_iter(self):
        word = Word('hello')
        i = iter(word)
        assert ''.join(i) == 'hello'
        with pytest.raises(StopIteration):
            next(i)
        assert ''.join(word) == 'hello'

    def test_contains(self):
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
        foo = Word('foo')
        assert foo == foo
        assert foo == Word('foo')
        assert foo == Word(foo)
        assert not (foo == Word('monkey'))

    def test_ne(self):
        assert Word('monkey') != Word('butler')
        assert Word('monkey') != 'monkey'
        assert not (Word('monkey') != Word('monkey'))

    def test_pop(self):
        w = Word('foo')
        assert w.pop('f') == 'f'
        assert str(w) == '.oo'
        assert w.pop('o') == 'o'
        assert str(w) == '..o'
        assert w.pop('o') == 'o'
        assert str(w) == '...'

    def test_pop_nonexistent(self):
        w = Word('foo')
        with pytest.raises(ValueError) as excinfo:
            w.pop('a')
        assert str(excinfo.value) == '"a" is not in word'

    def test_pop_single_letter_from_middle_of_word(self):
        w = Word('primary')
        assert w.pop('m') == 'm'
        assert str(w) == 'pri.ary'

    def test_pop_multiple_letters(self):
        w = Word('monkey')
        assert w.pop('onk') == 'onk'
        assert str(w) == 'm...ey'

    def test_len(self):
        key = 'key'
        assert len(Word(key)) == len(key)
        monkey = 'monkey'
        assert len(Word(monkey)) == len(monkey)
        w = Word(monkey)
        w.pop(key)
        assert len(w) == len(monkey) - len(key)

    def test_vowel_groups(self):
        assert list(Word('hello').vowel_groups()) == ['e', 'o']
        assert list(Word('monkey').vowel_groups()) == ['o', 'ey']
        assert list(Word('toast').vowel_groups()) == ['oa']
        assert list(Word('abomination').vowel_groups()) == \
            ['a', 'o', 'i', 'a', 'io']
        assert list(Word('unceremoniously').vowel_groups()) == \
            ['u', 'e', 'e', 'o', 'iou', 'y']
