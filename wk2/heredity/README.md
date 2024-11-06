# Heredity Simulator

### Implementation of a Bayesian network to assess the likelihood that a person will have a particular genetic trait based on their family data.

### Usage
```bash
$ python heredity.py [path_to_family_data]
```
### Example
```bash
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```

### Interpretation of Output
- Gene: probability of the person having x copies of the gene.
- Trait: probability that the person does/does not exhibit the trait.
- E.g. The probability of Harry having 0 copies of the gene is 0.5351, and the probability of him exhibiting the trait is 0.2665.

### Default Probabilities
1. Unconditional probabilities for having gene
    - 0 copies: 0.96
    - 1 copy: 0.03
    - 2 copies: 0.01
2. Probability of displaying the trait given x copies of the gene
    - 0 copies: 0.01
    - 1 copy: 0.56
    - 2 copies: 0.65
3. Mutation probability: 0.01

