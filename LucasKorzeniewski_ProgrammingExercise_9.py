class BankAcct:
    """A simple bank account class that tracks balance and interest."""

    def __init__(self, name, acct_num, amount, interest_rate):
        # Store the owner's name so statements can be personalized
        self.name = name

        # Store the account number as the unique account identifier
        self.acct_num = acct_num

        # Store the current balance so it can be adjusted and reported
        self.amount = amount

        # Store the interest rate as a decimal (e.g. 0.05 for 5 percent)
        self.interest_rate = interest_rate

    def deposit(self, deposit_amount):
        # Reject negative deposits so the balance can't be corrupted
        if deposit_amount < 0:
            print("Deposit amount must be positive.")
            return

        # Add the deposit to the current balance
        self.amount = self.amount + deposit_amount

    def withdraw(self, withdraw_amount):
        # Reject negative withdrawals so the balance can't be corrupted
        if withdraw_amount < 0:
            print("Withdrawal amount must be positive.")
            return

        # Block the withdrawal if there are insufficient funds
        if withdraw_amount > self.amount:
            print("Insufficient funds for this withdrawal.")
            return

        # Subtract the withdrawal from the current balance
        self.amount = self.amount - withdraw_amount

    def adjust_interest_rate(self, new_rate):
        # Reject a negative rate since interest can't be less than zero
        if new_rate < 0:
            print("Interest rate cannot be negative.")
            return

        # Update the stored rate to the new value
        self.interest_rate = new_rate

    def get_balance(self):
        # Return the current balance so callers can use it directly
        return self.amount

    def calc_interest(self, num_days):
        # Convert the annual rate to a daily rate for the calculation
        DAYS_PER_YEAR = 365

        # Multiply balance by daily rate and number of days to get interest
        interest = self.amount * self.interest_rate * \
            (num_days / DAYS_PER_YEAR)

        return interest

    def __str__(self):
        # Build a readable summary showing balance and interest details
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.acct_num}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate * 100:.2f}%"
        )


def test_bank_acct():
    """Exercise each BankAcct method and print the results."""

    # Create a new account to use for all the following tests
    my_account = BankAcct("Jordan Lee", "1001", 1000.00, 0.05)

    # Display the initial state of the account before any changes
    print("Initial account state:")
    print(my_account)
    print()

    # Test that a valid deposit increases the balance correctly
    my_account.deposit(250.00)
    print("After depositing $250.00:")
    print(my_account)
    print()

    # Test that a valid withdrawal decreases the balance correctly
    my_account.withdraw(100.00)
    print("After withdrawing $100.00:")
    print(my_account)
    print()

    # Test that an over-withdrawal is rejected and balance is unchanged
    print("Attempting to withdraw $5000.00:")
    my_account.withdraw(5000.00)
    print(my_account)
    print()

    # Test that the interest rate can be adjusted successfully
    my_account.adjust_interest_rate(0.07)
    print("After adjusting interest rate to 7%:")
    print(my_account)
    print()

    # Test the balance getter method against the known current amount
    print(f"Current balance via get_balance(): "
          f"${my_account.get_balance():.2f}")
    print()

    # Test the interest calculation over a 30 day period
    thirty_day_interest = my_account.calc_interest(30)
    print(f"Interest earned over 30 days: ${thirty_day_interest:.2f}")
    print()

    # Test the interest calculation over a full 365 day year
    yearly_interest = my_account.calc_interest(365)
    print(f"Interest earned over 365 days: ${yearly_interest:.2f}")


if __name__ == "__main__":
    # Run the test function only when this file is executed directly
    test_bank_acct()