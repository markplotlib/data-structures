import unittest
import linked_list as ll


class MyTestCase(unittest.TestCase):
    def test_ctor_no_args_head_is_none(self):
        # arrange

        # act
        ll0: object = ll.LinkedList()

        # assert
        self.assertIsNone(ll0.head)

    def test_ctor_1_arg_head_is_not_none(self):
        # arrange
        n1 = ll.Node(123)

        # act
        ll1: object = ll.LinkedList(n1)

        # assert
        self.assertIsNotNone(ll1.head)

    def test_ctor_no_args_length_is_0(self):
        # arrange

        # act
        ll0: object = ll.LinkedList()

        # assert
        self.assertEqual(ll0.length, 0)

    def test_ctor_1_arg_length_is_1(self):
        # arrange
        n1 = ll.Node(123)

        # act
        ll1: object = ll.LinkedList(n1)

        # assert
        self.assertEqual(ll1.length, 1)


if __name__ == '__main__':
    unittest.main()
