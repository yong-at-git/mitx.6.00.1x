class W2P2Solution:
    pass


def calc_fixed_monthly_payment(balance, annualInterestRate):
    """
    :param balance:
    :param annualInterestRate:
    :return:
    """
    guess = 10

    while calc_annual_balance_with_fixed_monthly_pay(balance, annualInterestRate, guess) > 0:
        guess += 10

    return guess


def calc_annual_balance_with_fixed_monthly_pay(balance, annualInterestRate, monthlyFixedPayment):
    """
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    :param balance:
    :param annualInterestRate:
    :return:
    """
    monthly_interest_rate = annualInterestRate / 12.0
    current_balance = balance
    month = 1
    while month <= 12:
        monthly_unpaid_balance = current_balance - monthlyFixedPayment
        current_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        month += 1
    rounded_year_end_balance = round(current_balance, 2)
    print("Remaining balance:", rounded_year_end_balance)

    return rounded_year_end_balance


def calc_fixed_monthly_payment_v2(balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    remain_balance = balance
    guess = 0

    while remain_balance > 0:
        remain_balance = balance
        guess += 10
        month = 1
        while month <= 12:
            monthly_unpaid_balance = remain_balance - guess
            remain_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            month += 1

    print("Lowest Payment:", guess)


def round_by(num, base):
    return (round(num) // round(base)) * round(base)
