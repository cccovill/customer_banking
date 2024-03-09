# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account 
from savings_account import create_savings_account 
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
updated_savings_balance = (float)
savings_balance = (float)
balance_prompt = False
interest_prompt = False
month_prompt = False
while balance_prompt == False:
    entered_savings_bal = input("Enter savings_balance, in both dollars and cents '(Ex. $100.25 = 100.25)' - ..$")
    b = entered_savings_bal.split(".")       # isolate dollars and cents (remove .) 
    c = b[0]+b[1]                            # Combine dollars and cents without decimal
    if c.isdigit():                          #  Test if all numeric
        savings_balance = float(entered_savings_bal)
        balance_prompt = True
    else:
        print ("Invalid entry. A non-numeric entry was made.")
while interest_prompt == False:
    entered_interest_rate = input("Enter interest '(APR)' rate: Ex. 5 1/4% : enter - 525..")
    if entered_interest_rate.isdigit():
        savings_rate = float(entered_interest_rate)
        interest_prompt = True
    else:
        print ("Invalid entry. A non-numeric entry was made.")
while month_prompt == False:
    entered_month = input("Enter term '(in months)' for Account..")
    if entered_month.isdigit():
        savings_maturity = int(entered_month)
        month_prompt = True
        if savings_maturity == 0 :
            month_prompt = False        
            print("Invalid month.  Must be greater than zero'(0)'") 
        else:
            month_prompt = True
            print (f"Edit checks complete. Balance = ${savings_balance} ; Rate = {savings_rate / 10000:.4f} ; Months = {savings_maturity} ")
    else:
        month_prompt = False  
        print ("Invalid entry.  Must be numeric")  
    
    # Call the create_savings_account function and pass the variables from the user.
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"The new savings balance including acrrued interest of ${interest_earned:.2f} is ${updated_savings_balance:.2f}. ")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
balance_prompt = False
interest_prompt = False
month_prompt = False
while balance_prompt == False:
    entered_savings_bal = input("Enter cd_balance..")
    if entered_savings_bal.isdigit():
        cd_balance = int(entered_savings_bal)
        balance_prompt = True
    else:
        print ("Invalid entry. A non-numeric entry was made.")
while interest_prompt == False:
    entered_interest_amt = input("Enter interest amount..")
    if entered_interest_amt.isdigit():
        cd_interest = int(entered_interest_amt)
        interest_prompt = True
    else:
        print ("Invalid entry. A non-numeric entry was made.")
while month_prompt == False:
    entered_month = input("Enter term '(in months)' for CD")
    if entered_month.isdigit():
        cd_maturity = int(entered_month)
        month_prompt = True
        if cd_maturity == 0 :
            month_prompt = False        
            print("Invalid month.  Must be greater than zero'(0)'") 
        else:
            month_prompt = True
            print("Edit checks complete. Processing continues.")
    else:
        month_prompt = False  
        print ("Invalid entry.  Must be numeric") 
    # Call the create_cd_account function and pass the variables from the user.
updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"At maturity, the balance including acrrued interest of ${interest_earned:.2f} is ${updated_cd_balance:.2f}. ")


if __name__ == "__main__":
    # Call the main function.
    main()