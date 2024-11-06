# Pagerank Algorithm

### This project calculates PageRank values for a set of web pages, implementing both the Sampling and Iterative methods to estimate the importance of each page in a given corpus.

### Usage
```bash
$ python pagerank.py [corpus_directory]
```

### Example
```bash
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```
This output shows the PageRank for each page using both methods, which should produce similar results for a given corpus.

### Key Concepts
- Sampling Method: Estimates PageRank by simulating a random surfer moving through the corpus based on the transition model.
- Iterative Method: Uses a mathematical formula to update PageRank values iteratively until they converge, providing a stable rank for each page.

### Files and Structure
- pagerank.py: Contains the main PageRank calculations and core functions for implementing both sampling-based and iterative PageRank methods.
- corpus: A folder with sample HTML files representing pages and links to help test the program’s PageRank calculations.

### Constants
- DAMPING: The damping factor (default 0.85), representing the likelihood that a random surfer will follow a link rather than randomly choosing a page.
- SAMPLES: The number of samples (default 10000) to use for estimating PageRank through the sampling method.