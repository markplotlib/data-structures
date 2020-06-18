import unittest
from heap import Heap


class MyTestCase(unittest.TestCase):
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



if __name__ == '__main__':
    unittest.main()
