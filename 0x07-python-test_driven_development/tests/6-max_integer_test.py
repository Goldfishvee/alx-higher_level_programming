#!/usr/bin/python3
"""Unittest  module for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_for_docstring(self):
        """Tests for module docstring"""
        dstr = __import__('6-max_integer').__doc__
        self.assertTrue(len(dstr) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        fstr = max_integer.__doc__
        self.assertTrue(len(fstr) > 1)

    def test_empty_list(self):
        """Test for an empty list []"""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Tests for supplying no argument to function"""
        self.assertIsNone(max_integer())

    def test_list_with_one_integer(self):
        """Test for supplying only one number in list"""
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_multiple_integers(self):
        """Tests for supplying multiple arguments"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_list_with_one_negative_integer(self):
        """Tests for one negative number in list"""
        self.assertEqual(max_integer([100, 50, 5, -7, 14, 60]), 100)

    def test_list_with_negative_integers(self):
        """Tests for supplying negative integers only"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_list_with_positive_max_at_begin(self):
        """Tests for positive max integer at beginning of list"""
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50]), 200)

    def test_list_with_positive_max_at_middle(self):
        """Tests for positive max integer in middle of list"""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_list_with_positive_max_at_end(self):
        """Tests for positive max integer at end of list"""
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)

    def test_list_none_argument(self):
        """Test for supplying none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_non_integer_argument(self):
        """Tests for a type non-int in list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "Hello", 4, 5])


if __name__ == "__main__":
    unittest.main()
