class W2P1Solution:
    @staticmethod
    def calc_annual_balance(balance, annualInterestRate, monthlyPaymentRate):
        """
        Monthly interest rate= (Annual interest rate) / 12.0
        Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
        Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
        Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        :param balance:
        :param annualInterestRate:
        :param monthlyPaymentRate:
        :return:
        """
        monthly_interest_rate = annualInterestRate / 12.0
        current_balance = balance
        month = 1
        while month <= 12:
            minimum_monthly_payment = monthlyPaymentRate * current_balance
            monthly_unpaid_balance = current_balance - minimum_monthly_payment
            current_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            month += 1
        rounded_year_end_balance = round(current_balance, 2)
        print("Remaining balance:", rounded_year_end_balance)

        return rounded_year_end_balance


