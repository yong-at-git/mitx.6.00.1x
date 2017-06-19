from unittest import TestCase
from p1_pay_debt_itr import W2P1Solution


class TestW2P1Solution(TestCase):
    def test_calc_annual_balance_case_1(self):
        """
            balance = 42
            annualInterestRate = 0.2
            monthlyPaymentRate = 0.04

            # Result Your Code Should Generate Below:
            Remaining balance: 31.38
        :return:
        """
        result = W2P1Solution.calc_annual_balance(42, 0.2, 0.04)
        self.assertEqual(31.38, result)

    def test_calc_annual_balance_case_2(self):
        """
            balance = 484
            annualInterestRate = 0.2
            monthlyPaymentRate = 0.04

            Result Your Code Should Generate Below:
            Remaining balance: 361.61
        :return:
        """
        result = W2P1Solution.calc_annual_balance(484, 0.2, 0.04)
        self.assertEqual(361.61, result)
