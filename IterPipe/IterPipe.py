from collections.abc import Iterator
import itertools
import functools
import operator


class IterPipe(Iterator):
    def __init__(self, iterator):
        self.iterator = iter(iterator)

    def __iter__(self):
        return self

    def __next__(self):
        return self.iterator.__next__()

    def accumulate(self, func=operator.add):
        """
        Return running accumulation as iterator.

        See https://docs.python.org/3.7/library/itertools.html#itertools.accumulate

        :param: func: An optional function to use for accumulation. Summing is used if not given.
        :type: callable
        :rtype: IterPipe
        """
        return IterPipe(itertools.accumulate(self, func))

    def all(self):
        """
        See https://docs.python.org/3/library/functions.html#all

        :rtype: bool
        """
        return all(self)

    def any(self):
        """
        See https://docs.python.org/3/library/functions.html#any
        
        :rtype: bool
        """
        return any(self)

    def chain(self, *iterables):
        """
        Chain given iterators to end of current IterPipe.

        See https://docs.python.org/3.7/library/itertools.html#itertools.chain

        :rtype: IterPipe
        """
        return IterPipe(itertools.chain(self, *iterables))

    def combinations(self, r: int):
        """
        Return successive r-length combinations of elements in the iterable.

        See https://docs.python.org/3.7/library/itertools.html#itertools.combinations

        :rtype: IterPipe
        """
        return IterPipe(itertools.combinations(self, r))

    def combinations_with_replacement(self, r: int):
        """
        Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.

        See https://docs.python.org/3.7/library/itertools.html#itertools.combinations_with_replacement

        :rtype: IterPipe
        """
        return IterPipe(itertools.combinations_with_replacement(self, r))

    def compress(self, selectors):
        """
        Return data elements corresponding to true selector elements. Forms a shorter iterator from selected data elements using the selectors to choose the data elements.

        See https://docs.python.org/3.7/library/itertools.html#itertools.compress
        :rtype: IterPipe
        """
        return IterPipe(itertools.compress(self, selectors))

    def cycle(self):
        """
        Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

        See https://docs.python.org/3.7/library/itertools.html#itertools.cycle
        :rtype: IterPipe
        """
        return IterPipe(itertools.cycle(self))

    def dict(self, **kwarg):
        """
        New dictionary initialized as if via:
            d = {} for k, v in iterable:
                d[k] = v

        See https://docs.python.org/3/library/functions.html#func-dict
        :rtype: dict
        """
        return dict(self, **kwarg)

    def dropwhile(self, predicate):
        """
        Drop items from the iterable while predicate(item) is true. Afterwards, return every element until the iterable is exhausted.

        See https://docs.python.org/3.7/library/itertools.html#itertools.dropwhile
        :rtype: IterPipe
        """
        return IterPipe(itertools.dropwhile(predicate, self))

    def enumerate(self, **kwarg):
        """
        The enumerate function yields pairs containing a count (from start, which defaults to zero) and a value yielded by the IterPipe.

        See https://docs.python.org/3/library/functions.html#enumerate
        :rtype: IterPipe
        """
        return IterPipe(enumerate(self, **kwarg))

    def filterfalse(self, predicate: callable):
        """
        Return those items of sequence for which function(item) is false. If function is None, return the items that are false

        See https://docs.python.org/3.7/library/itertools.html#itertools.filterfalse
        :rtype: IterPipe
        """
        return IterPipe(itertools.filterfalse(predicate, self))

    def frozenset(self):
        """
        Build an immutable unordered collection of unique elements

        See https://docs.python.org/3/library/functions.html#func-frozenset
        :rtype: frozenset
        """
        return frozenset(self)

    def filter(self, function: callable):
        """
        Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

        :return:
        """
        return IterPipe(filter(function, self))

    def groupby(self, key=None):
        """
        Make an iterator that returns consecutive keys and groups from the iterable. If the key function is not specified or is None, the element itself is used for grouping.

        See https://docs.python.org/3/library/itertools.html#itertools.groupby
        :rtype: IterPipe
        """
        return IterPipe(itertools.groupby(self, key))

    def islice(self, *args, **kwargs):
        """
        Return an iterator whose next() method returns selected values from an iterable. If start is specified, will skip all preceding elements; otherwise, start defaults to zero. Step defaults to one. If specified as another value, step determines how many values are skipped between successive calls. Works like a slice() on a list but returns an iterator.

        https://docs.python.org/3/library/itertools.html#itertools.islice
        :rtype: IterPipe
        """
        return IterPipe(itertools.islice(self, *args, **kwargs))

    def list(self):
        """
        Convert iterator to list
        :rtype: list
        """
        return list(self)

    def map(self, function):
        """
        Apply the given function to each item in the iterator
        :rtype: IterPipe
        """
        return IterPipe(map(function, self))

    def max(self, *args, **kwargs):
        """
        Return the biggest item in the iterator. The default keyword-only argument specifies an object to return if the provided iterable is empty

        See https://docs.python.org/3/library/functions.html#max
        """
        return max(self, *args, **kwargs)

    def min(self, *args, **kwargs):
        """
        Return the smallest item in the iterator. The default keyword-only argument specifies an object to return if the provided iterable is empty

        See https://docs.python.org/3/library/functions.html#min
        """
        return min(self, *args, **kwargs)

    def next(self):
        """
        Return the next item from the iterator.

        See https://docs.python.org/3/library/functions.html#next
        """
        return next(self)

    def permutations(self, r=None):
        """
        Return successive r-length permutations of elements in the iterable

        See https://docs.python.org/3.7/library/itertools.html#itertools.permutations
        :rtype: IterPipe
        """
        return IterPipe(itertools.permutations(self, r=r))

    def product(self, *iterables, repeat=1):
        """
        Cartesian product of input iterables. Equivalent to nested for-loops.

        See https://docs.python.org/3.7/library/itertools.html#itertools.product
        :rtype: IterPipe
        """
        return IterPipe(itertools.product(self, *iterables, repeat=repeat))

    def set(self):
        """
        Convert iterator to set

        See https://docs.python.org/3/library/functions.html#func-set
        :rtype: set
        """

        return set(self)

    def sorted(self, key=None, reverse=False):
        """
        Return a new iterator containing all items in ascending order

        See https://docs.python.org/3/library/functions.html#sorted
        :rtype: IterPipe
        """
        return IterPipe(sorted(self, key=key, reverse=reverse))

    def starmap(self, function):
        """
        Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.

        See https://docs.python.org/3.7/library/itertools.html#itertools.starmap
        """
        return IterPipe(itertools.starmap(function, self))

    def sum(self, *args):
        """
        Return the sum of a 'start' value (default: 0) plus an iterable of numbers

        See https://docs.python.org/3/library/functions.html#sum
        """
        return sum(self, *args)

    def takewhile(self, predicate):
        """
        Return successive entries as long as the predicate evaluates to true for each entry

        See https://docs.python.org/3.7/library/itertools.html#itertools.takewhile
        :rtype: IterPipe
        """
        return IterPipe(itertools.takewhile(predicate, self))

    def tee(self, n=2):
        """
        Return tuple of n independent iterators

        See https://docs.python.org/3.7/library/itertools.html#itertools.tee
        """
        return itertools.tee(self, n)

    def tuple(self):
        """
        Convert iterator to tuple

        See https://docs.python.org/3/library/functions.html#func-tuple
        """
        return tuple(self)

    def zip(self, *iterables):
        """Zip the iterator with provided iterables

        See https://docs.python.org/3/library/functions.html#zip
        :rtype: IterPipe
        """
        return zip(self, *iterables)

    def zip_longest(self, *iterables, fillvalue=None):
        """

        See https://docs.python.org/3.7/library/itertools.html#itertools.zip_longest
        :param args:
        :param kwargs:
        :return:
        """
        return IterPipe(itertools.zip_longest(self, *iterables, fillvalue=fillvalue))


    def reduce(self, function, initializer=None):
        """
        Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value.

        See https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce
        """
        return functools.reduce(function, self, initializer)