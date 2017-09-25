# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:29:20 2017

@author: Seth Guberman - sguberman@gmail.com
"""

from collections import defaultdict
from parse import mhyph_dict_from_file, mpos_dict_from_file


def words_by_syllable():
    """
    Build an index of all words with n syllables.
    """
    print('Building n-syllable lookup table...')

    words = defaultdict(list)

    for word, syllables in mhyph_dict_from_file().items():
        words[syllables].append(word)

    print('Done!')

    return words


def words_by_part_of_speech():
    """
    Build an index of all words with a given part of speech.
    """
    print('Building parts of speech lookup table...')

    words = defaultdict(list)

    for word, pos in mpos_dict_from_file().items():
        for symbol in pos:
            words[symbol].append(word)

    print('Done!')

    return words


def query_intersection(n, pos, syllable_dict=None, pos_dict=None):
    """
    Return the intersection (set) of all words with n syllables and given part
    of speech.
    """
    if syllable_dict is None:
        syllable_dict = words_by_syllable()
    if pos_dict is None:
        pos_dict = words_by_part_of_speech()

    return set(syllable_dict[n]).intersection(set(pos_dict[pos]))


if __name__ == '__main__':
    words_with_n_syllables = words_by_syllable()
    words_with_part_of_speech = words_by_part_of_speech()
