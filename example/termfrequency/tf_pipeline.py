"""Compute term frequencies for an input file using a pipeline style"""
# Refactor all of this source code so that it fully adheres
# to the source code standard for the Python programming language

# !/usr/bin/env python
import re
import operator
import string

#
# The functions
#


from typing import Dict, List, Tuple
def read_file(path_to_file: str) -> str:
    """
    Takes a path to a file and returns the entire
    contents of the file as a string
    """
    with open(path_to_file) as f:
        data = f.read()
    return data


def filter_chars_and_normalize(str_data: str) -> str:
    """
    Takes a string and returns a copy with all non-alphanumeric
    chars replaced by white space
    """
    pattern = re.compile(r"[\W_]+")
    return pattern.sub(" ", str_data).lower()


def scan(str_data: str) -> List[str]:
    """
    Takes a string and scans for words, returning
    a list of words.
    """
    return str_data.split()


def remove_stop_words(word_list: List[str]) -> List[str]:
    """
    Takes a list of words and returns a copy with all stop
    words removed
    """
    with open("stopwords/stop_words.txt") as f:
        stop_words = f.read().split(",")
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if w not in stop_words]


def frequencies(word_list: List[str]) -> Dict[str, int]:
    """
    Takes a list of words and returns a dictionary associating
    words with frequencies of occurrence
    """
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs


def sort(word_freq: Dict[str, int]) -> List[Tuple[str, int]]:
    """
    Takes a dictionary of words and their frequencies
    and returns a list of pairs where the entries are
    sorted by frequency
    """
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)


def print_all(word_freqs: List[Tuple[str, int]]) -> None:
    """
    Takes a list of pairs where the entries are sorted by frequency and print them recursively.
    """
    if word_freqs != " ":
        for tf in word_freqs:
            print(tf[0], " - ", tf[1])


def run(sysarg: str) -> None:
    """
    Function to run all the functions
    """
    print_all(
        sort(
            frequencies(
                remove_stop_words(
                    scan(filter_chars_and_normalize(read_file(sysarg)))
                )
            )
        )[0:25]
    )
