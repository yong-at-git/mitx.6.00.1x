class W2P3Solution:
    pass


def calc_minimum_monthly_payment_bisection_search(balance, annualInterestRate):
    """
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
    :return:
    """
    lower_bound = balance / 12
    monthly_interest_rate = annualInterestRate / 12.0
    upper_bound = (balance * ((1 + monthly_interest_rate)**12)) / 12
    guess = lower_bound + (upper_bound - lower_bound) / 2
    rounded_guess = round(guess, 2)
    step = 0.01

    while True:
        if calc_annual_balance_with_fixed_monthly_pay(balance, monthly_interest_rate, rounded_guess) > 0:
            if calc_annual_balance_with_fixed_monthly_pay(balance, monthly_interest_rate, rounded_guess + step) < 0:
                rounded_guess += step
                break
            lower_bound = rounded_guess
            rounded_guess = round((lower_bound + (upper_bound - lower_bound) / 2), 2)

        if calc_annual_balance_with_fixed_monthly_pay(balance, monthly_interest_rate, rounded_guess) < 0:
            if calc_annual_balance_with_fixed_monthly_pay(balance, monthly_interest_rate, rounded_guess - step) > 0:
                rounded_guess -= step
                break
            upper_bound = rounded_guess
            rounded_guess = round((lower_bound + (upper_bound - lower_bound) / 2), 2)

    print("Lowest Payment:", rounded_guess)
    return rounded_guess


def calc_annual_balance_with_fixed_monthly_pay(balance, monthly_interest_rate, monthlyFixedPayment):
    """
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    :param balance:
    :param monthly_interest_rate:
    :return:
    """
    current_balance = balance
    month = 1
    while month <= 12:
        monthly_unpaid_balance = current_balance - monthlyFixedPayment
        current_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
        month += 1
    rounded_year_end_balance = round(current_balance, 2)
    print("Remaining balance:", rounded_year_end_balance)

    return rounded_year_end_balance


def calc_minimum_monthly_payment_bisection_search_v2(balance, annual_interest_rate):
    lower_bound = balance / 12
    monthly_interest_rate = annual_interest_rate / 12.0
    upper_bound = (balance * ((1 + monthly_interest_rate) ** 12)) / 12
    guess = lower_bound + (upper_bound - lower_bound) / 2
    guess = round(guess, 2)
    step = 0.01

    while True:
        remain_balance = balance
        month = 1
        while month <= 12:
            monthly_unpaid_balance = remain_balance - guess
            remain_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
            month += 1

        if remain_balance > 0:
            remain_balance = balance
            month = 1
            guess += step
            while month <= 12:
                monthly_unpaid_balance = remain_balance - guess
                remain_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
                month += 1
            if remain_balance < 0:
                break
            lower_bound = guess - step
            guess = round((lower_bound + (upper_bound - lower_bound) / 2), 2)
        else:
            remain_balance = balance
            month = 1
            guess -= step
            while month <= 12:
                monthly_unpaid_balance = remain_balance - guess
                remain_balance = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
                month += 1
            if remain_balance > 0:
                break
            upper_bound = guess + step
            guess = round((lower_bound + (upper_bound - lower_bound) / 2), 2)

    print("Lowest Payment:", round(guess, 2))
    return guess
