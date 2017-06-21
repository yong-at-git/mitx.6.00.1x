from unittest import TestCase
from p3_pay_debt_bisection_search import *


class TestW2P3Solution(TestCase):
    def test_calc_minimum_monthly_payment_bisection_search_case_1(self):
        """
        balance = 320000
        annualInterestRate = 0.2

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 29157.09
        :return:
        """
        actual = calc_minimum_monthly_payment_bisection_search(320000, 0.2)
        self.assertEqual(29157.09, actual)

    def test_calc_minimum_monthly_payment_bisection_search_case_2(self):
        """
        balance = 999999
        annualInterestRate = 0.18

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 90325.03
        :return:
        """
        actual = calc_minimum_monthly_payment_bisection_search(999999, 0.18)
        self.assertEqual(90325.03, actual)

    def test_calc_minimum_monthly_payment_bisection_search_v2_case_1(self):
        """
        balance = 320000
        annualInterestRate = 0.2

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 29157.09
        :return:
        """
        actual = calc_minimum_monthly_payment_bisection_search_v2(320000, 0.2)
        self.assertEqual(29157.09, actual)

    def test_calc_minimum_monthly_payment_bisection_search_v2_case_2(self):
        """
        balance = 999999
        annualInterestRate = 0.18

        Result Your Code Should Generate:
        -------------------
        Lowest Payment: 90325.03
        :return:
        """
        actual = calc_minimum_monthly_payment_bisection_search_v2(999999, 0.18)
        self.assertEqual(90325.03, actual)
