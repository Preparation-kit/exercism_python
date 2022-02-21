#!/usr/bin/python3
"""
Unittest
"""

import unittest


from hello_world import (
    hello,
)


class HelloWorldTest(unittest.TestCase):
    """
    test_say_hi
    """

    def test_say_hi(self):
        """
        test_say_hi
        """
        self.assertEqual(hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
