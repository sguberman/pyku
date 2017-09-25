# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:12:20 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def mhyph_dict_from_file(filename='mhyph.txt', delim='`'):
    """
    Parse the mhyph file and return a dictionary of word -> syllables.
    """
    print('...Building dictionary of syllables... ', end='')

    mhyph_dict = {}

    with open(filename, 'r') as f:

        for line in f:
            spaces = line.count(' ')
            dashes = line.count('-')
            hyphenation = line.strip().split(delim)
            syllables = len(hyphenation) + spaces + dashes
            word = ''.join(hyphenation)
            mhyph_dict[word] = syllables

    print('Done!')

    return mhyph_dict


def mpos_dict_from_file(filename='mpos.txt', delim=', '):
    """
    Parse the mpos file and return a dictionary of word -> parts of speech.
    """
    print('...Building dictionary of parts of speech... ', end='')

    mpos_dict = {}

    with open(filename, 'r') as f:

        for line in f:
            word, pos = line.strip().split(', ')
            mpos_dict[word] = pos

    print('Done!')

    return mpos_dict
