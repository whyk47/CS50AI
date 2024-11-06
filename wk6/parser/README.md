# Parser

### Overview
The goal of this project is to build a natural language processing (NLP) tool that can parse English sentences and extract noun phrases (NPs). Using context-free grammar (CFG) rules, the parser will generate syntactic trees and identify noun phrase chunks in a sentence. The project leverages the NLTK (Natural Language Toolkit) library for tokenization and tree manipulation.

### Usage
1. Install the required dependencies using the following command:
```bash
$ pip install -r requirements.txt
```
2. Run the parser with the following command:
```bash
$ python parser.py
```
3. Input a sentence with user input.

### Example
```bash
$ python parser.py
Sentence: I had a little moist red paint in the palm of my hand.
              S
  ____________|______________________
 |                                   VP
 |    _______________________________|________________
 |   |               NP                               |
 |   |    ___________|_______________                 |
 |   |   |          AdjP             |                PP
 |   |   |     ______|____           |         _______|________
 |   |   |    |          AdjP        |        PP               PP
 |   |   |    |       ____|____      |     ___|___          ___|___
 NP  |   |    |      |        AdjP   |    |       NP       |       NP
 |   |   |    |      |         |     |    |    ___|___     |    ___|___
 N   V  Det  Adj    Adj       Adj    N    P  Det      N    P  Det      N
 |   |   |    |      |         |     |    |   |       |    |   |       |
 i  had  a  little moist      red  paint  in the     palm  of  my     hand

Noun Phrase Chunks
i
a little moist red paint
the palm
my hand
```
