#DON'T MAKE CHANGES TO THIS FILE

#write tests for all the questions here

import unittest

from tests.question_tests import question_tests

suite = unittest.TestLoader().loadTestsFromModule(question_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

def test_get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
        self.assertEqual(41, get_fahrenheit(5))
        self.assertEqual(50, get_fahrenheit(10))

def test_get_bonus_pay_amount(self):
        self.assertEqual(ValueError, get_bonus_pay_amount(-1))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        self.assertEqual(ValueError, get_bonus_pay_amount(2000))

def test_get_random_number(self):
        for x in range(5):
                num = get_random_number(1, 5)
                self.assertEqual(True, (num >= 1))
                self.assertEqual(True, (num <= 5))