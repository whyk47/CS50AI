# Degrees

### Overview
The Degrees project identifies the shortest path between two actors based on their connections through movies. This project uses a breadth-first search algorithm to find the minimum degree of separation between two actors.

### Usage:
1. Run the program by specifying a dataset directory.
2. Enter the names of two actors.
3. The program outputs the shortest path in degrees and lists each movie connection.
```bash
$ python degrees.py [dataset]
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

### Project Structure
1. CSV Files:
    - people.csv: Contains actor data (unique id, name, birth year).
    - movies.csv: Contains movie data (id, title, year).
    - stars.csv: Maps actor ids to movie ids (defines actor participation in films).
2. Program Files:
    - degrees.py: The main program file, which loads data, prompts user input, and finds actor connections.
    - util.py: Contains supporting classes for search functionality (Node, StackFrontier, QueueFrontier).