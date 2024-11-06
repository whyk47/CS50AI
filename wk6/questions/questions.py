import nltk
from nltk.tokenize import word_tokenize
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():
    nltk.download('stopwords')

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    print('Loading files...')
    txt_files = dict()
    root_dir = os.getcwd()
    txt_dir = os.path.join(os.getcwd(), directory)
    os.chdir(txt_dir)
    for filename in os.listdir(txt_dir):
        with open(filename, 'r', encoding="utf8") as txt_file:
            txt_files[filename] = txt_file.read()
    os.chdir(root_dir)
    return txt_files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    print('Tokenising...')
    words = word_tokenize(document.lower())
    for word in words.copy():
        if word in list(nltk.corpus.stopwords.words("english")) or not set(word).difference(set(string.punctuation)):
            words.remove(word)
    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    print('Computing IDFs...')
    num_docs = len(documents)
    words = set()
    for text in list(documents.values()):
        words = words.union(set(text))
    idf = {
        word: math.log(num_docs / len([text[0] for text in list(documents.values()) if word in text]))
        for word in words
    }
    return idf


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    print('Picking top files...')
    tf_idf = {
        file: sum([files[file].count(word) * idfs[word] for word in query])
        for file in list(files.keys())
    }
    tf_idf = dict(sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)[:n])
    return(list(tf_idf.keys()))


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    matching_word_measure = {
        sentence: sum([idfs[word] for word in query if word in sentences[sentence]])
        for sentence in list(sentences.keys())
    }
    matching_word_measure = dict(sorted(matching_word_measure.items(), key=lambda x: (x[1], query_term_density(query, sentences[x[0]])), reverse=True)[:n])
    return list(matching_word_measure.keys())


def query_term_density(query, sentence):
    total_words = len(sentence)
    counter = 0
    for word in sentence:
        if word in query:
            counter += 1
    return counter / total_words



if __name__ == "__main__":
    main()
