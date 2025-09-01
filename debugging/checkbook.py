#!/usr/bin/python3
"""
Checkbook Program

This program simulates a simple checkbook with deposit,
withdrawal, and balance-checking functionality via CLI.
"""


class Checkbook:
    """
    A simple checkbook class to track
    balance with deposit and withdrawal methods.

    Attributes:
        balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """Initialize the checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to be deposited.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook,
        if sufficient funds are available.

        Parameters:
            amount (float): The amount to be withdrawn.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main function to interact with the user
    and perform actions on the checkbook."""
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be a positive number.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be a positive number.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
