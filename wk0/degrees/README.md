# Degrees

### Finds the shortest path between any two actors by choosing a sequence of movies that connects them using Breadth First Search. 

### Usage:
```bash
$ python degrees.py [dataset_size (large/small)]
Loading data...
Data loaded.
Name: {actor_name_1}
Name: {actor_name_2}
```

### Example:
```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```
