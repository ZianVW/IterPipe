# IterPipe
## Introduction
This is a wrapper for the iterator functions in the Python Standard Library to make it easier and more readable to chain them together into a pipeline.

It is a way to implement Martin Fowler's _Collection Pipeline_ pattern (https://martinfowler.com/articles/collection-pipeline/) with Python's standard iterator functions.

To illustrate the concept, we will perform the following sequence of steps in each example:

1. Start with a `range` iterator,
2. Then `filter` to pass only the values larger or equal to 6
3. Then square each number from step 2, using the `map` function
4. Then `sum` the squares from step 3

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
    # Simple function to
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
    # Simple function to
    return x * x

input = range(10)

output = (IterPipe(input) 
          .filter(filter_func)
          .map(squared)
          .sum()
          )
          
print("Output with IterPipe chaining: {output}".format(output=output))
``` 

The IterPipe wrapper supports the built-in functions that operate on iterators, as well as the functions in the `itertools` library.

## Installation

Works with Python 3.4 or later.

```
pip install -U IterPipe
```