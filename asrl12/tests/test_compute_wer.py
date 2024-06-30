import pytest

from asrl12.get_WER import compute_wer


def test_compute_wer_exact():
    assert compute_wer(["hello"], ["hello"]) == 0.0


def test_compute_wer_substitution():
    assert compute_wer(["hello"], ["hallo"]) == 1.0


def test_compute_wer_insertion():
    wer = compute_wer(["I", "am", "tired"], ["I", "am", "very", "tired"])
    assert pytest.approx(wer) == 1/3


def test_compute_wer_deletion():
    wer = compute_wer(["I", "am", "very", "tired"], ["I", "am", "tired"])
    assert pytest.approx(wer) == 1/4


def test_compute_wer_mixed():
    wer = compute_wer(["I", "am", "tired"], ["I", "was", "really", "tired"])
    assert pytest.approx(wer) == 2/3
    