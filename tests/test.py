
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
        from ham.symbols import __all__
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
        assert set(__all__) == set(symbols)
