"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    SavingsAccount = Account(balance, interest_rate)
 

    # Calculate interest earned
    updated_balance = 0 
    earned_interest = 0
    wbalance = float(balance) 
    winterest_rt = float(interest_rate)
    wmonths = int(months) 

     # ADD YOUR CODE HERE
    percent_rate = winterest_rt / 100  # shift decimal right by 4
    monthly_irate = percent_rate / 12    # divide for monthly rate
    earned_interest = (wbalance * monthly_irate * wmonths)     
        
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = wbalance + earned_interest
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.set_interest(earned_interest)
    # Return the updated balance and interest earned.
    return(updated_balance, earned_interest)  # ADD YOUR CODE HERE
