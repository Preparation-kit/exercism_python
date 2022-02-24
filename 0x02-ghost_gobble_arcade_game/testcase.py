#!/usr/bin/env python3
"""
Unittest
"""

import unittest


from arcade import (
    eat_ghost,
    score,
    lose,
    win,
)


class GuidosGorgeousLasagnaTest(unittest.TestCase):
    """
    test_say_hi
    """

    def test_expected_bake_time(self):
        """
        test_say_hi
        """
        self.assertIs(eat_ghost(False, True))

    def test_bake_time_remaining_t(self):
        """
        test_say_hi
        """
        self.assertIs(eat_ghost(True, False))

    def test_docstrings_were_written(self):
        """
        test_say_hi
        """
        self.assertIs(eat_ghost(True, True))

    def test_preparation_time_in_minutes(self):
        """
        test
        """
        self.assertIs(score(False, False))

    def test_elapsed_time_in_minutes(self):
        """test
        """
        self.assertIs(score(False, True))


if __name__ == "__main__":
    unittest.main()
