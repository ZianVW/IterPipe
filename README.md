# IterPipe
![Build Status](https://travis-ci.org/ZianVW/IterPipe.svg?branch=master)
[![codecov](https://codecov.io/gh/ZianVW/IterPipe/branch/master/graph/badge.svg)](https://codecov.io/gh/ZianVW/IterPipe)
[![PyPi version](https://pypip.in/v/IterPipe/badge.png)](https://crate.io/packages/$REPO/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/92990c1cc30349459a00253ad646e8eb)](https://www.codacy.com/app/Cognizon/IterPipe?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ZianVW/IterPipe&amp;utm_campaign=Badge_Grade)

## Introduction
This is a wrapper for the iterator functions in the Python Standard Library to make it easier and more readable to chain them together into a pipeline.

It is a way to implement Martin Fowler's _Collection Pipeline_ pattern ([https://martinfowler.com/articles/collection-pipeline/]) with Python's standard iterator functions.

To illustrate the concept, we will perform the following sequence of steps in each example:

1.  Start with a `range` iterator,
2.  Then `filter` to pass only the values larger or equal to 6
3.  Then square each number from step 2, using the `map` function
4.  Then `sum` the squares from step 3

Here is the code, using intermediate variables, without chaining.
```python
def filter_func(x):
    # Simple function used in "filter" examples below
    return x >= 6


def squared(x):
    # Simple function to square it's input.  Used in "map" below.
    return x * x

input = range(10)

intermediate_1 = filter(filter_func, input)

# Apply squared function to each value returned by intermediate_1 iterator
intermediate_2 = map(squared, intermediate_1)

output = sum(intermediate_2)

print("Output without chaining: {output}".format(output=output))
```

Here is the same code, using regular Python syntax chaining. Note that execution happens inside-out, with the last operation (sum) appearing first.
```python
def filter_func(x):
    return x >= 6


def squared(x):
    # Simple function to square it's input.  Used in "map" below.
    return x * x

input = range(10)

output = sum(map(squared, filter(filter_func, input)))

print("Output with regular Python chaining: {output}".format(output=output))
```

And here is the same code again, using the `IterPipe` wrapper. Note that it reads in the same order as execution happens.
```python
from IterPipe import IterPipe

def filter_func(x):
    return x >= 6


def squared(x):
    # Simple function to square it's input.  Used in "map" below.
    return x * x

input = range(10)

output = (IterPipe(input) 
          .filter(filter_func)
          .map(squared)
          .sum()
          )
          
print("Output with IterPipe chaining: {output}".format(output=output))
``` 

The IterPipe wrapper supports the following functions that operate on iterators from `builtins`, `itertools` and `functools`.

+   accumulate
+   all
+   any
+   chain
+   combinations
+   combinations_with_replacement
+   compress
+   cycle
+   dict
+   dropwhile
+   enumerate
+   filter
+   filterfalse
+   frozenset
+   groupby
+   islice
+   iterator
+   list
+   map
+   max
+   min
+   next
+   permutations
+   product
+   reduce
+   set
+   sorted
+   starmap
+   sum
+   takewhile
+   tee
+   tuple
+   zip
+   zip_longest

## Installation

Works with Python 3.4 or later.

```bash
pip install -U IterPipe
```