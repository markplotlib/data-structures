import unittest
from heap import Heap


class MyTestCase(unittest.TestCase):
    # full test coverage of constructor in 6 cases
    def test_ctor_noargs_attr_wgts_empty(self):
        # act
        hp = Heap()
        # assert
        self.assertEqual(hp.weights, {})

    def test_ctor_noargs_attr_place_empty(self):
        # act
        hp = Heap()
        # assert
        self.assertEqual(hp.place, {})

    def test_ctor_noargs_attr_heap_empty(self):
        # act
        hp = Heap()
        # assert
        self.assertEqual(hp.heap, [])

    def test_ctor_1arg_attr_wgts_equal(self):
        # arrange
        initial = {'a': 1}
        # act
        hp = Heap(initial)
        # assert
        self.assertEqual(hp.weights, {'a': 1})

    def test_ctor_1arg_attr_place_equal(self):
        # arrange
        initial = {'a': 1}
        # act
        hp = Heap(initial)
        # assert
        self.assertEqual(hp.place, {'a': 0})

    def test_ctor_1arg_attr_heap_equal(self):
        # arrange
        initial = {'a': 1}
        # act
        hp = Heap(initial)
        # assert
        self.assertEqual(hp.heap, ['a'])

    # full test coverage of empty in 2 cases
    def test_empty_length_is_0(self):
        # arrange
        hp = Heap()
        # assert
        self.assertTrue(hp.empty())

    def test_empty_length_is_1(self):
        # arrange
        hp = Heap({'a': 1})
        # assert
        self.assertFalse(hp.empty())

    # full test coverage of enqueue in 4 cases
    def test_enqueue_key_is_present(self):
        # arrange
        hp = Heap({'a': 1, 'b': 10, 'c': 20})
        # act
        hp.enqueue('a', 1)
        # assert
        self.assertEqual(hp.weights['a'], 1)

    def test_enqueue_key_is_new(self):
        # arrange
        hp = Heap({'a': 1, 'b': 10, 'c': 20})
        # act
        hp.enqueue('d', 50)
        # assert
        self.assertEqual(hp.weights['d'], 50)

    def test_enqueue_key_old_wgt_is_greater(self):
        # arrange
        hp = Heap({'a': 5, 'b': 10, 'c': 20})
        # act
        hp.enqueue('a', 1)
        # assert
        self.assertEqual(hp.weights['a'], 1)

    def test_enqueue_key_old_wgt_is_lesser(self):
        # arrange
        hp = Heap({'a': 2, 'b': 10, 'c': 20})
        # act
        hp.enqueue('a', 10)
        # assert
        self.assertEqual(hp.weights['a'], 10)


if __name__ == '__main__':
    unittest.main()
