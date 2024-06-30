# Automatic Speech Recognition (ASR) Evaluation: Word Error Rate on Transcriptions from Speakers with Different First Languages

Compare the Word Error Rate between different ASR transcriptions.

Linyu Zhang

## Introduction

The performance of Automatic Speech Recognition (ASR) systems has demonstrated impressive improvement over recent years (Chiu et al., 2018). Many researches have already showed that the ASR systems have almost reached human-level speech recognition (Xiong et al., 2017; Edwards et al., 2017). However, high performance level are often achieved on data obtained from strictly controlled environment and native speakers (Panayotov et al., 2015). 

In order to evaluate the quality of a speech recognition system, Word Error Rate (WER) is often used as the standard. It is defined as the number of inserted, substituted or deleted words in the ASR output compared to a reference transcript, divided by the length of the reference. It is easily computed using a Levenshtein distance of the two word sequences. 

This program will let you compute the average WER of any transcriptions from ASR systems of your choice, and compare these results. For example, comparing WER of Whisper transcriptions from several L2 English speakers whose L1 is Mandarin and speakers whose L1 is Cantonese. 


## Installation

Install this package using [poetry](https://python-poetry.org/docs/#installation) by running

    poetry install


## Usage

Assuming `ENG_ENG`, `CMN_ENG`, and `CCT_ENG` are three folders containing English transcriptions in text files from Whisper of the same content created by speakers with different first languages: English, Chinese Mandarin, and Cantonese, respectively, the reference text file is  NWS_English.txt. You can compute the average WER of speakers with each first language and compare them as follows:

    poetry run python asrl12/main.py ENG_ENG CMN_ENG CCT_ENG NWS_English.txt

If you only have 1 folder or more than 3 folders, just delete or add the folders, such as

    poetry run python asrl12/main.py CMN_ENG NWS_English.txt

    poetry run python asrl12/main.py ENG_ENG CMN_ENG CCT_ENG CSP_ENG CTW_ENG NWS_English.txt

For further options, see

    python main.py --help


## Data

The `data` directory contains folders `hypothesis` and `reference`. 

In folder `hypothesis`, English transcriptions from Whisper, a state-of-the-art automatic speech recognition system produced by Open AI (Radford et al., 2023), are divided into folders named with speakers' first language and second language. 

Folder `reference` contains a text file, which is the standard English version of the story North Wind and the Sun. All speakers were required to read the story in natural speech rate. 

The original audio files together with the text file are from ALLSSTAR corpus, available at https://speechbox.linguistics.northwestern.edu/ALLSSTARcentral/#!/recordings.


## References

Chiu et al. 2018. State-of-the-art speech recognition with sequence-to-sequence models. In proceedings of 2018 IEEE international conference on acoustics, speech and signal processing (ICASSP),
pages 4774-4778.

Edwards et al. 2017. Medical speech recognition: reaching parity with humans. In proceedings of Speech and Computer: 19th International Conference,
pages 512-524, Hatfield, UK.

Panayotov et al. 2015. Librispeech: an asr corpus based on public domain audio books. In proceedings of 2015 IEEE international conference on acoustics, speech and signal processing (ICASSP),
pages 5206-5210.

Radford et al. 2023. Robust speech recognition via large-scale weak supervision. In proceedings of International Conference on Machine Learning,
pages 28493-28518.

Xiong et al. 2017. Toward human parity in conversational speech recognition. 
IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2017, 25(12): 2410-2423.

