# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 00:04:13 2017

@author: Seth Guberman - sguberman@gmail.com
"""


def mpos(delim=', '):
    """
    Reformat the original Moby parts of speech file into plain ascii text.

    delim: (str) delimiter to use in the output file
    """
    print('Reformatting parts of speech file...')

    with open('mpos/mobyposi.txt', 'rb') as orig, open('mpos.txt', 'w') as mod:

        orig_bytes = orig.read()
        count = 0
        skipped = 0

        for line in orig_bytes.split(b'\r'):  # original file has \r lines
            try:
                # Split on the original delimiter and decode to str
                word, tag = (x.decode() for x in line.split(b'\xd7'))
                mod.write('{}{}{}\n'.format(word, delim, tag))
                count += 1
            except UnicodeDecodeError:  # weird character in entry
                skipped += 1
            except ValueError:  # weird line in file
                pass

        print('...Reformatted {} entries, skipped {}.'.format(count, skipped))


def mhyph(delim='`'):
    """
    Reformat the original Moby hyphenates file to plain ascii text.

    delim: (str) delimitter to use in the output file
    """
    print('Reformatting original hyphenates file...')

    with open('mhyph/mhyph.txt', 'rb') as orig, open('mhyph.txt', 'w') as mod:

        orig_bytes = orig.read()
        count = 0
        skipped = 0

        for line in orig_bytes.split(b'\r\n'):
            try:
                syllables = (x.decode() for x in line.split(b'\xa5'))
                mod.write('{}\n'.format(delim.join(syllables)))
                count += 1
            except UnicodeDecodeError:  # weird character in entry
                skipped += 1
            except ValueError:  # weird line in file
                pass

        print('...Reformatted {} entries, skipped {}.'.format(count, skipped))


if __name__ == '__main__':
    mpos()
    mhyph()
