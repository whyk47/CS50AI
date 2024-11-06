# Questions

### Overview
The "Questions" project aims to develop an AI system that can answer user queries based on a set of text documents. The system employs techniques from Natural Language Processing (NLP), specifically tf-idf (Term Frequency-Inverse Document Frequency), to retrieve relevant documents and passages in response to user queries. The project focuses on document retrieval and passage retrieval by ranking files and sentences according to their relevance to the query.

### Example Usage
1. Install dependencies.
```bash
$ pip install -r requirements.txt
```
2. Run the program specifying the corpus directory.
3. Input your question.
```bash
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning, classification, and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.
```

### Project Workflow
1. Document Loading: The `load_files` function reads the .txt files from the corpus directory and stores their contents.
2. Tokenization: The `tokenize` function processes the documents by breaking them into individual words, filtering out unnecessary characters (punctuation, stopwords), and normalizing to lowercase.
3. IDF Calculation: The `compute_idfs` function calculates the IDF for each word based on its frequency across all documents, helping to identify words that are more informative.
4. Document Ranking: The `top_files` function ranks documents by summing the tf-idf values of words that appear in both the query and the document.
5. Sentence Ranking: The `top_sentences` function ranks sentences by the sum of IDF values for query words and their "query term density" (the proportion of query words in the sentence).
