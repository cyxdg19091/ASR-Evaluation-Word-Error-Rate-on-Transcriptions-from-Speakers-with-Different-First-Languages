import os

from typing import TextIO
from asrl12.get_WER import compute_wer


def read_text_file(file_path: TextIO):
    """
    Read the contents from a text file and return as a list of words.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower().split()


def average_wer(reference_file_path: TextIO, hypothesis_folder_path: TextIO):
    """
    Compute the average Word Error Rate (WER) for multiple hypothesis files against a single reference file.
    """
    reference_text = read_text_file(reference_file_path)
    wer_values = []
    for file_name in os.listdir(hypothesis_folder_path):
        if file_name.endswith(".txt"):
            hypothesis_file_path = os.path.join(hypothesis_folder_path, file_name)
            hypothesis_text = read_text_file(hypothesis_file_path)
            wer = compute_wer(reference_text, hypothesis_text)
            wer_values.append(wer)
    if wer_values:
        return sum(wer_values) / len(wer_values)
    else:
        return None 
