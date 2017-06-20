from unittest import TestCase
from p2_pay_debt_fixed_montly_pay import *


class TestW2P2Solution(TestCase):
    def test_round_by(self):
        self.assertEqual(0, round_by(3, 5))
        self.assertEqual(0, round_by(3.3, 5.2))
        self.assertEqual(10, round_by(13, 5))
        self.assertEqual(15, round_by(17, 5))
        self.assertEqual(0, round_by(3, 10))
        self.assertEqual(0, round_by(3.7, 10))
        self.assertEqual(10, round_by(13, 10))
        self.assertEqual(110, round_by(113, 10))

    def test_calc_fixed_monthly_payment_case_1(self):
        """
        Test Case 1:
        balance = 3329
        annualInterestRate = 0.2

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 310
        :return:
        """
        self.assertEqual(310, calc_fixed_monthly_payment(3329, 0.2))

    def test_calc_fixed_monthly_payment_case_2(self):
        """
        Test Case 2:
        balance = 4773
        annualInterestRate = 0.2

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 440
        :return:
        """
        self.assertEqual(440, calc_fixed_monthly_payment(4773, 0.2))

    def test_calc_fixed_monthly_payment_case_3(self):
        """
        Test Case 3:
        balance = 3926
        annualInterestRate = 0.2

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 360
        :return:
        """
        self.assertEqual(360, calc_fixed_monthly_payment(3926, 0.2))