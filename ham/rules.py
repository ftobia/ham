
def match_ng(pairing):
    most_recent_index = 0
    while 'ng' in pairing.word and 'NG' in pairing.pronunciation:
        pairing.word.pop('ng')
        index = pairing.pronunciation.index('NG', most_recent_index)
        most_recent_index = index + 1
        pairing.phonograms[index] += 'ng'


def match_p(pairing):
    most_recent_index = 0
    while 'p' in pairing.word and 'P' in pairing.pronunciation:
        pairing.word.pop('p')
        index = pairing.pronunciation.index('P', most_recent_index)
        most_recent_index = index + 1
        pairing.phonograms[index] += 'p'


def match_equal_phonemes_and_letters(pairing):
    pass
