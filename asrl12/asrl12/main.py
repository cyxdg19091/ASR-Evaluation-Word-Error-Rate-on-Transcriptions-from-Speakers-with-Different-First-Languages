"""
Compare the average Word Error Rate (WER) between the reference text and texts in any number of folders.
"""
from argparse import ArgumentParser

from asrl12.aver_WER import average_wer


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Calculate the average Word Error Rate (WER) for multiple hypothesis text files against a single reference file.")
    parser.add_argument(
        'folders', 
        type=str, 
        nargs='+', 
        help="Folders (at least one) containing hypothesis text files",
    )
    parser.add_argument(
        'reference', 
        type=str,
        help="A single reference text file",
    )
    return parser


def main():
    # Parse command line arguments
    parser = get_argument_parser()
    args = parser.parse_args()
    # Get average WER of the texts in each folder
    reference_text = args.reference
    hypothesis_folders = args.folders
    results = {}
    for hypothesis_folder in hypothesis_folders:
        wer = average_wer(reference_text, hypothesis_folder)
        results[hypothesis_folder] = wer
        if wer is not None:
            print(f"The average WER for {hypothesis_folder} is: {wer * 100:.2f}%")
        else:
            print(f"No valid text files found in {hypothesis_folder}.")
    # Print a comparison, get the lowest and highest WER
    if results:
        min_wer = min(results, key=results.get)  
        max_wer = max(results, key=results.get)
        print(f"'{min_wer}' has the lowest WER of {results[min_wer] * 100:.2f}%", 
              f"\n'{max_wer}' has the highest WER of {results[max_wer] * 100:.2f}%")


if __name__ == "__main__":
    main()
