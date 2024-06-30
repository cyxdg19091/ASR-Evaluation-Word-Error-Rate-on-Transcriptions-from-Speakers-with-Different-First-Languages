import pytest

from asrl12.get_WER import levenshtein_distance


def test_levenshtein_distance_exact():
    assert levenshtein_distance(["hello"], ["hello"]) == 0


def test_levenshtein_distance_substitution():
    assert levenshtein_distance(["hello"], ["hallo"]) == 1


def test_levenshtein_distance_insertion():
    assert levenshtein_distance(["I", "am", "tired"], ["I", "am", "very", "tired"]) == 1


def test_levenshtein_distance_deletion():
    assert levenshtein_distance(["I", "am", "very", "tired"], ["I", "am", "tired"]) == 1
