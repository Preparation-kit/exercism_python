#!/usr/bin/env python3
"""
Unittest
"""

import unittest


from lasagna import (
    bake_time_remaining,
    preparation_time_in_minutes,
    elapsed_time_in_minutes,
    EXPECTED_BAKE_TIME,
)


class GuidosGorgeousLasagnaTest(unittest.TestCase):
    """
    test_say_hi
    """

    def test_expected_bake_time(self):
        """
        test_say_hi
        """
        failure_msg = 'Expected a constant of EXPECTED_BAKE_TIME with value of 40'
        self.assertEqual(EXPECTED_BAKE_TIME, 40, msg=failure_msg)

    def test_bake_time_remaining_t(self):
        """
        test_say_hi
        """
        input_data = [1, 2, 5, 10, 15, 23, 33, 39]
        result_data = [40 - item for item in input_data]

        test = zip(input_data, result_data)

        for variant, (time, result) in enumerate(test, start=1):
            with self.subTest(f'variation #{variant}', time=time, result=result):
                failure_msg = f'Expected: {result} but the bake time remaining was calculated incorrectly.'
                self.assertEqual(bake_time_remaining(
                    time), result, msg=failure_msg)

    def test_docstrings_were_written(self):
        """
        test_say_hi
        """
        functions = [bake_time_remaining,
                     preparation_time_in_minutes, elapsed_time_in_minutes]

        for variant, function in enumerate(functions, start=1):
            with self.subTest(f'variation #{variant}', function=function):
                failure_msg = f'Expected a docstring for `{function.__name__}`, but received `None` instead.'
                self.assertIsNotNone(function.__doc__, msg=failure_msg)

    def test_preparation_time_in_minutes(self):
        """
        test
        """
        input_data = [1, 2, 5, 8, 11, 15]
        result_data = [item * 2 for item in input_data]

        for variant, (layers, time) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', layers=layers, time=time):
                failure_msg = f'Expected: {time} minutes, but preparation time was calculated incorrectly.'
                self.assertEqual(preparation_time_in_minutes(
                    layers), time, msg=failure_msg)

    def test_elapsed_time_in_minutes(self):
        """test
        """
        layer_data = (1, 2, 5, 8, 11, 15)
        time_data = (3, 7, 8, 4, 15, 20)
        result_data = [prep * 2 + elapsed for prep,
                       elapsed in zip(layer_data, time_data)]

        for variant, (layers, time, total_time) in enumerate(zip(layer_data, time_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', layers=layers, time=time, total_time=total_time):
                failure_msg = f'Expected {time} minutes elapsed, but the timing was calculated incorrectly.'
                self.assertEqual(elapsed_time_in_minutes(
                    layers, time), total_time, msg=failure_msg)


if __name__ == "__main__":
    unittest.main()
