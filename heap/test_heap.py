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


if __name__ == '__main__':
    unittest.main()
