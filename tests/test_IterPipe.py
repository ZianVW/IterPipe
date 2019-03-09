import unittest

from IterPipe import IterPipe


class test_Iterpipe(unittest.TestCase):
    def test_roundtrip(self):
        # Simple round-trip test
        input = [1, 2, 3]
        output = list(IterPipe(input))
        self.assertEqual(input, output)

    def test_accumulate(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .accumulate()
                      )
        self.assertEqual(output, [1, 3, 6])

    def test_all(self):
        input = [True, True]
        output = (IterPipe(input)
                  .all()
                  )
        self.assertTrue(output)

    def test_any(self):
        input = [True, False]
        output = (IterPipe(input)
                  .any()
                  )
        self.assertTrue(output)

    def test_chain(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .chain([4, 5, 6])
                      )
        self.assertEqual(output, [1, 2, 3, 4, 5, 6])

    def test_combinations(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .combinations(2)
                      )
        self.assertEqual(output, [(1, 2), (1, 3), (2, 3)])

    def test_combinations_with_replacement(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .combinations_with_replacement(2)
                      )
        self.assertEqual(output, [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)])

    def test_compress(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .compress([1, 0, 0])
                      )
        self.assertEqual(output, [1])

    def test_cycle(self):
        input = [1, 2, 3]
        iterator = (IterPipe(input)
                    .cycle()
                    )
        output = [next(iterator) for _ in range(6)]
        self.assertEqual(output, [1, 2, 3, 1, 2, 3])

    def test_dict(self):
        input = [("a", 1), ("b", 2)]
        output_1 = (IterPipe(input)
                    .dict()
                    )
        self.assertEqual(output_1, {"a": 1, "b": 2})

        output_2 = (IterPipe(input)
                    .dict(c=3)
                    )
        self.assertEqual(output_2, {"a": 1, "b": 2, "c": 3})

    def test_dropwhile(self):
        input = [1, 2, 3]
        predicate = lambda x: x <= 2
        output = list(IterPipe(input)
                      .dropwhile(predicate)
                      )
        self.assertEqual(output, [3])

    def test_enumerate(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .enumerate()
                      )
        self.assertEqual(output, [(0, 1), (1, 2), (2, 3)])

    def test_filterfalse(self):
        input = [1, 2, 3]
        predicate = lambda x: x == 2
        output = list(IterPipe(input)
                      .filterfalse(predicate)
                      )
        self.assertEqual(output, [1, 3])

    def test_frozenset(self):
        input = [1, 2, 3]
        output = (IterPipe(input)
                  .frozenset()
                  )
        self.assertEqual(output, frozenset([1, 2, 3]))

    def test_filter(self):
        input = [1, 2, 3]
        predicate = lambda x: x == 2
        output = list(IterPipe(input)
                      .filter(predicate)
                      )
        self.assertEqual(output, [2])

    def test_groupby(self):
        input = [(1, "a"), (1, "b"), (2, "c"), (2, "d")]
        key = lambda x: x[0]
        groups = (IterPipe(input)
                  .groupby(key)
                  )
        output = [(i[0], list(i[1])) for i in groups]
        self.assertEqual(output, [(1, [(1, "a"), (1, "b")]),
                                  (2, [(2, "c"), (2, "d")])])

    def test_islice(self):
        input = [1, 2, 3, 4]
        output = list(IterPipe(input)
                      .islice(1, 3)
                      )
        self.assertEqual(output, [2, 3])

    def test_list(self):
        input = [1, 2, 3]
        output = (IterPipe(input)
                  .list()
                  )
        self.assertEqual(input, output)

    def test_map(self):
        input = [1, 2, 3]
        function = lambda x: x * 2
        output = list(IterPipe(input)
                      .map(function)
                      )
        self.assertEqual(output, [2, 4, 6])

    def test_max(self):
        input = [1, 2, 3]
        output_1 = (IterPipe(input)
                    .max()
                    )
        self.assertEqual(output_1, 3)

        input = [(1, "a"), (2, "b"), (3, "c")]
        key = lambda x: x[0]
        output_2 = (IterPipe(input)
                    .max(key=key)
                    )
        self.assertEqual(output_2, (3, "c"))

    def test_min(self):
        input = [1, 2, 3]
        output_1 = (IterPipe(input)
                    .min()
                    )
        self.assertEqual(output_1, 1)

        input = [(1, "a"), (2, "b"), (3, "c")]
        key = lambda x: x[0]
        output_2 = (IterPipe(input)
                    .min(key=key)
                    )
        self.assertEqual(output_2, (1, "a"))

    def test_next(self):
        input = [1, 2, 3]
        iter_pipe = (IterPipe(input))
        output_1 = iter_pipe.next()
        self.assertEqual(output_1, 1)
        output_2 = iter_pipe.next()
        self.assertEqual(output_2, 2)

    def test_permutations(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .permutations(r=2)
                      )
        self.assertEqual(output, [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

    def test_product(self):
        input = [1, 2]
        output = list(IterPipe(input)
                      .product([3, 4])
                      )
        self.assertEqual(output, [(1, 3), (1, 4), (2, 3), (2, 4)])

    def test_set(self):
        input = [1, 2, 1]
        output = (IterPipe(input)
                  .set())
        self.assertEqual(output, {1, 2})

    def test_sorted(self):
        input_1 = [3, 2, 1]
        output_1 = list(IterPipe(input_1)
                        .sorted()
                        )
        self.assertEqual(output_1, [1, 2, 3])

        input_2 = [(3, "c"), (2, "b"), (1, "a")]
        key = lambda x: x[0]
        output_2 = list(IterPipe(input_2)
                        .sorted(key=key)
                        )
        self.assertEqual(output_2, [(1, "a"), (2, "b"), (3, "c")])

    def test_starmap(self):
        input = [(1, 1), (2, 2)]
        function = lambda x, y: x + y
        output = list(IterPipe(input)
                      .starmap(function)
                      )
        self.assertEqual(output, [2, 4])

    def test_sum(self):
        input = [1, 2, 3]
        output = (IterPipe(input)
                  .sum()
                  )
        self.assertEqual(output, 6)

    def test_takewhile(self):
        input = [1, 2, 3]
        predicate = lambda x: x <= 2
        output = list(IterPipe(input)
                      .takewhile(predicate)
                      )
        self.assertEqual(output, [1, 2])

    def test_tee(self):
        input = [1, 2, 3]
        (iter_pipe_1, iter_pipe_2) = (IterPipe(input)
                                      .tee(2)
                                      )
        output_1 = list(iter_pipe_1)
        self.assertEqual(output_1, input)
        output_2 = list(iter_pipe_2)
        self.assertEqual(output_2, input)

    def test_tuple(self):
        input = [1, 2, 3]
        output = (IterPipe(input)
                  .tuple()
                  )
        self.assertEqual(output, (1, 2, 3))

    def test_zip(self):
        input = [1, 2, 3]
        output = list(IterPipe(input)
                      .zip([4, 5, 6])
                      )
        self.assertEqual(output, [(1, 4), (2, 5), (3, 6)])

    def test_zip_longest(self):
        input_1 = [1, 2, 3]
        output_1 = list(IterPipe(input_1)
                        .zip_longest([4, 5])
                        )
        self.assertEqual(output_1, [(1, 4), (2, 5), (3, None)])

        input_1 = [1, 2, 3]
        output_1 = list(IterPipe(input_1)
                        .zip_longest([4, 5], fillvalue=99)
                        )
        self.assertEqual(output_1, [(1, 4), (2, 5), (3, 99)])


