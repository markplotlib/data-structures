import unittest
import linked_list as ll


class MyTestCase(unittest.TestCase):
    def test_ctor_no_args_head_is_none(self):
        ll0: object = ll.LinkedList()
        self.assertIsNone(ll0.head)


if __name__ == '__main__':
    unittest.main()
