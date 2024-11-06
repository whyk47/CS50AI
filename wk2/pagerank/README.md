# Pagerank Algorithm

### Given a corpus of webpages, calculate the PageRank of each page. The PageRank of a given page is the probability that a random surfer will end up on that page. A website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less. 

### Usage
```bash
$ python pagerank.py [corpus]
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

### Interpretation
- Results from Sampling: the proportion of visits for each page from following links at random.
- Results from iteration: Probability of visiting each page based on iteratively applying the recursive Pagerank formula.