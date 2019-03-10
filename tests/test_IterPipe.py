import unittest

from IterPipe import IterPipe


class test_Iterpipe(unittest.TestCase):
    def test_roundtrip(self):
        # Simple round-trip test
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable))
        self.assertEqual(input_iterable, output)

    def test_accumulate(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .accumulate()
                      )
        self.assertEqual(output, [1, 3, 6])

    def test_all(self):
        input_iterable = [True, True]
        output = (IterPipe(input_iterable)
                  .all()
                  )
        self.assertTrue(output)

    def test_any(self):
        input_iterable = [True, False]
        output = (IterPipe(input_iterable)
                  .any()
                  )
        self.assertTrue(output)

    def test_chain(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .chain([4, 5, 6])
                      )
        self.assertEqual(output, [1, 2, 3, 4, 5, 6])

    def test_combinations(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .combinations(2)
                      )
        self.assertEqual(output, [(1, 2), (1, 3), (2, 3)])

    def test_combinations_with_replacement(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .combinations_with_replacement(2)
                      )
        self.assertEqual(output, [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)])

    def test_compress(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .compress([1, 0, 0])
                      )
        self.assertEqual(output, [1])

    def test_cycle(self):
        input_iterable = [1, 2, 3]
        iterator = (IterPipe(input_iterable)
                    .cycle()
                    )
        output = [next(iterator) for _ in range(6)]
        self.assertEqual(output, [1, 2, 3, 1, 2, 3])

    def test_dict(self):
        input_iterable = [("a", 1), ("b", 2)]
        output_1 = (IterPipe(input_iterable)
                    .dict()
                    )
        self.assertEqual(output_1, {"a": 1, "b": 2})

        output_2 = (IterPipe(input_iterable)
                    .dict(c=3)
                    )
        self.assertEqual(output_2, {"a": 1, "b": 2, "c": 3})

    def test_dropwhile(self):
        input_iterable = [1, 2, 3]
        predicate = lambda x: x <= 2
        output = list(IterPipe(input_iterable)
                      .dropwhile(predicate)
                      )
        self.assertEqual(output, [3])

    def test_enumerate(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .enumerate()
                      )
        self.assertEqual(output, [(0, 1), (1, 2), (2, 3)])

    def test_filterfalse(self):
        input_iterable = [1, 2, 3]
        predicate = lambda x: x == 2
        output = list(IterPipe(input_iterable)
                      .filterfalse(predicate)
                      )
        self.assertEqual(output, [1, 3])

    def test_frozenset(self):
        input_iterable = [1, 2, 3]
        output = (IterPipe(input_iterable)
                  .frozenset()
                  )
        self.assertEqual(output, frozenset([1, 2, 3]))

    def test_filter(self):
        input_iterable = [1, 2, 3]
        predicate = lambda x: x == 2
        output = list(IterPipe(input_iterable)
                      .filter(predicate)
                      )
        self.assertEqual(output, [2])

    def test_groupby(self):
        input_iterable = [(1, "a"), (1, "b"), (2, "c"), (2, "d")]
        key = lambda x: x[0]
        groups = (IterPipe(input_iterable)
                  .groupby(key)
                  )
        output = [(i[0], list(i[1])) for i in groups]
        self.assertEqual(output, [(1, [(1, "a"), (1, "b")]),
                                  (2, [(2, "c"), (2, "d")])])

    def test_islice(self):
        input_iterable = [1, 2, 3, 4]
        output = list(IterPipe(input_iterable)
                      .islice(1, 3)
                      )
        self.assertEqual(output, [2, 3])

    def test_list(self):
        input_iterable = [1, 2, 3]
        output = (IterPipe(input_iterable)
                  .list()
                  )
        self.assertEqual(input_iterable, output)

    def test_map(self):
        input_iterable = [1, 2, 3]
        function = lambda x: x * 2
        output = list(IterPipe(input_iterable)
                      .map(function)
                      )
        self.assertEqual(output, [2, 4, 6])

    def test_max(self):
        input_iterable = [1, 2, 3]
        output_1 = (IterPipe(input_iterable)
                    .max()
                    )
        self.assertEqual(output_1, 3)

        input_iterable = [(1, "a"), (2, "b"), (3, "c")]
        key = lambda x: x[0]
        output_2 = (IterPipe(input_iterable)
                    .max(key=key)
                    )
        self.assertEqual(output_2, (3, "c"))

    def test_min(self):
        input_iterable = [1, 2, 3]
        output_1 = (IterPipe(input_iterable)
                    .min()
                    )
        self.assertEqual(output_1, 1)

        input_iterable = [(1, "a"), (2, "b"), (3, "c")]
        key = lambda x: x[0]
        output_2 = (IterPipe(input_iterable)
                    .min(key=key)
                    )
        self.assertEqual(output_2, (1, "a"))

    def test_next(self):
        input_iterable = [1, 2, 3]
        iter_pipe = (IterPipe(input_iterable))
        output_1 = iter_pipe.next()
        self.assertEqual(output_1, 1)
        output_2 = iter_pipe.next()
        self.assertEqual(output_2, 2)

    def test_permutations(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .permutations(r=2)
                      )
        self.assertEqual(output, [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

    def test_product(self):
        input_iterable = [1, 2]
        output = list(IterPipe(input_iterable)
                      .product([3, 4])
                      )
        self.assertEqual(output, [(1, 3), (1, 4), (2, 3), (2, 4)])

    def test_set(self):
        input_iterable = [1, 2, 1]
        output = (IterPipe(input_iterable)
                  .set())
        self.assertEqual(output, {1, 2})

    def test_sorted(self):
        input_iterable_1 = [3, 2, 1]
        output_1 = list(IterPipe(input_iterable_1)
                        .sorted()
                        )
        self.assertEqual(output_1, [1, 2, 3])

        input_iterable_2 = [(3, "c"), (2, "b"), (1, "a")]
        key = lambda x: x[0]
        output_2 = list(IterPipe(input_iterable_2)
                        .sorted(key=key)
                        )
        self.assertEqual(output_2, [(1, "a"), (2, "b"), (3, "c")])

    def test_starmap(self):
        input_iterable = [(1, 1), (2, 2)]
        function = lambda x, y: x + y
        output = list(IterPipe(input_iterable)
                      .starmap(function)
                      )
        self.assertEqual(output, [2, 4])

    def test_sum(self):
        input_iterable = [1, 2, 3]
        output = (IterPipe(input_iterable)
                  .sum()
                  )
        self.assertEqual(output, 6)

    def test_takewhile(self):
        input_iterable = [1, 2, 3]
        predicate = lambda x: x <= 2
        output = list(IterPipe(input_iterable)
                      .takewhile(predicate)
                      )
        self.assertEqual(output, [1, 2])

    def test_tee(self):
        input_iterable = [1, 2, 3]
        (iter_pipe_1, iter_pipe_2) = (IterPipe(input_iterable)
                                      .tee(2)
                                      )
        output_1 = list(iter_pipe_1)
        self.assertEqual(output_1, input_iterable)
        output_2 = list(iter_pipe_2)
        self.assertEqual(output_2, input_iterable)

    def test_tuple(self):
        input_iterable = [1, 2, 3]
        output = (IterPipe(input_iterable)
                  .tuple()
                  )
        self.assertEqual(output, (1, 2, 3))

    def test_zip(self):
        input_iterable = [1, 2, 3]
        output = list(IterPipe(input_iterable)
                      .zip([4, 5, 6])
                      )
        self.assertEqual(output, [(1, 4), (2, 5), (3, 6)])

    def test_zip_longest(self):
        input_iterable_1 = [1, 2, 3]
        output_1 = list(IterPipe(input_iterable_1)
                        .zip_longest([4, 5])
                        )
        self.assertEqual(output_1, [(1, 4), (2, 5), (3, None)])

        input_iterable_1 = [1, 2, 3]
        output_1 = list(IterPipe(input_iterable_1)
                        .zip_longest([4, 5], fillvalue=99)
                        )
        self.assertEqual(output_1, [(1, 4), (2, 5), (3, 99)])

    def test_reduce(self):
        input_iterable = [1, 2, 3, 4]

        reduce_func = lambda x, y: x + y

        output = (IterPipe(input_iterable)
                  .reduce(reduce_func, 0)
                  )

        self.assertEqual(output, 10)
