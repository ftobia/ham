from ham import Word, Pronunciation, SoundPairing


class TestRules(object):

    def test_match_ng(self):
        from ham.rules import match_ng
        sp1 = SoundPairing('young', ['Y', 'AH1', 'NG'])
        match_ng(sp1)
        assert sp1.phonograms == ['', '', 'ng']
        assert str(sp1.word) == 'you..'
        sp2 = SoundPairing('tinge', ['T', 'IH1', 'N', 'JH'])
        match_ng(sp2)
        assert sp2.phonograms == ['', '', '', '']
        assert str(sp2.word) == 'tinge'
        sp3 = SoundPairing('winged', ['W', 'IH1', 'NG', 'D'])
        match_ng(sp3)
        assert sp3.phonograms == ['', '', 'ng', '']
        assert str(sp3.word) == 'wi..ed'
        sp4 = SoundPairing('singing', ['S', 'IH1', 'NG', 'IH0', 'NG'])
        match_ng(sp4)
        assert sp4.phonograms == ['', '', 'ng', '', 'ng']
        assert str(sp4.word) == 'si..i..'

    def test_match_p(self):
        from ham.rules import match_p
        sp1 = SoundPairing('pop', ['P', 'AA1', 'P'])
        match_p(sp1)
        assert sp1.phonograms == ['p', '', 'p']
        assert str(sp1.word) == '.o.'
        sp2 = SoundPairing('pink', ['P', 'IH1', 'NG', 'K'])
        match_p(sp2)
        assert sp2.phonograms == ['p', '', '', '']
        assert str(sp2.word) == '.ink'

    # def test_match_equal_phonemes_and_letters(self):
    #     from ham.rules import match_equal_phonemes_and_letters
    #     sp1 = SoundPairing('pop', ['P', 'AA1', 'P'])
    #     match_equal_phonemes_and_letters(sp1)
    #     assert sp1.phonograms == ['p', 'o', 'p']
    #     assert str(sp1.word) == '...'
