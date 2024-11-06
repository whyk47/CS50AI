import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable, words in list(self.domains.items()):
            for word in words.copy():
                if len(word) != variable.length:
                    self.domains[variable].remove(word)

	
    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revision = False
        # tuple (i, j), where  ith character of x must be the same as the jth character of y
        overlap = self.crossword.overlaps[x, y]
        if overlap == None:
            return revision
        for word_x in self.domains[x].copy():
            # list of y values with overlap
            possible_y_values = [word_y for word_y in self.domains[y] if word_x[overlap[0]] == word_y[overlap[1]]]
            if len(possible_y_values) == 0:
                self.domains[x].remove(word_x)
                revision = True
        return revision
                

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        function AC-3(csp):
        """
        """
        queue = all arcs in csp
        while queue non-empty:
            (X, Y) = Dequeue(queue)
            if Revise(csp, X, Y):
                if size of X.domain == 0:
                    return false
                for each Z in X.neighbors - {Y}:
                    Enqueue(queue, (Z,X))
        return true
        """
        if arcs == None:
            arcs = [arc for arc in list(self.crossword.overlaps.keys())]
        while arcs:
            (x, y) = arcs.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                arcs += [(z, x) for z in self.crossword.neighbors(x).difference({y})]
        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if all([bool(value) for value in list(assignment.values())]):
            return True
        else:
            return False


    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # check if all words are unique
        if sorted([value for value in assignment.values() if value]) != sorted(list({value for value in assignment.values() if value})):
            return False
        # check if all words are of correct length
        if not all([bool(var.length == len(word)) for var, word in list(assignment.items()) if word]):
            return False
        # check if all overlaps satisfied
        if not all([bool(assignment[vars[0]][overlap[0]] == assignment[vars[1]][overlap[1]]) for vars, overlap in list(self.crossword.overlaps.items()) if (overlap and assignment[vars[0]] and assignment[vars[1]])]):
            return False
        return True


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        overlaps = [(vars, overlap) for vars, overlap in list(self.crossword.overlaps.items()) if (overlap and var == vars[0])]
        constraints = dict()
        for value in self.domains[var]: # domain of current variable
            constraints[value] = 0
            for vars, overlap in overlaps: # iterate through all overlaps 
                for val in self.domains[vars[1]]: # domain of neighbouring variable
                    if value[overlap[0]] != val[overlap[1]]:
                        constraints[value] += 1
        return sorted(constraints, key=constraints.get)


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # list of all unassigned vars
        vars = [var for var in list(assignment.keys()) if not assignment[var]]
        # sort vars by length of domain (asc), then by number of neighbours (desc)
        vars = sorted(vars, key=lambda var: (len(self.domains[var]), - len(self.crossword.neighbors(var)))) 
        return vars[0]


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        """
        function Backtrack(assignment, csp):
          if assignment complete:
              return assignment
          var = Select-Unassigned-Var(assignment, csp)
          for value in Domain-Values(var, assignment, csp):
              if value consistent with assignment:
                  add {var = value} to assignment
                  inferences = Inference(assignment, csp)
                  if inferences ≠ failure:
                  add inferences to assignment
                  result = Backtrack(assignment, csp)
                  if result ≠ failure:
                      return result
                  remove {var = value} from assignment
          return failure
        """
        if assignment == {}:
            assignment = {
                var: None
                for var in list(self.domains.keys())
            }
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                # get arcs of var
                arcs = [arc for arc in list(self.crossword.overlaps.keys()) if var == arc[1]]
                # maintain arc consistency
                original = assignment.copy()
                inferences = self.ac3(arcs=arcs)
                if not inferences:
                    assignment = original
                result = self.backtrack(assignment)
                if result:
                    return result
            assignment[var] = None
        return None



def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
