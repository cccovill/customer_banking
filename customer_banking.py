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
    entered_savings_bal = input("Enter savings balance, in both dollars and cents '(Ex. $100.25 = 100.25)' - ..$")
    isdecimal = entered_savings_bal.find(".")
    how_many = entered_savings_bal.count('.')   # Get count of decimals
    if how_many > 1:
       print ("Invalid entry. A non-numeric entry was made.") 
       balance_prompt = False
    else: 
        if isdecimal == -1 :           # Now check if any cents was entered (all numeric, no decimal)
            print(f'Does not look as though any cents was entered.')
            balance_prompt = False
        else:
            b = entered_savings_bal.split(".")       # isolate dollars and cents (remove .) 
            c = b[0]+b[1]                            # Combine dollars and cents without decimal                     
            if c.isdigit():                          #  Test if all numeric
                savings_balance = float(entered_savings_bal)
                balance_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")
while interest_prompt == False:
    print(f'Enter Interest "(APR)" rate as a whole number and fraction thereof:')
    entered_interest_rate = input("Ex. 5 1/4% : enter - 5.25; Ex for 6 7/8 : enter 6.875 ..%")    
    isdecimal = entered_interest_rate.find(".")   # any fraction ? 
    how_many = entered_interest_rate.count('.')   # Get count of decimals
    if how_many > 1:
       print ("Invalid entry. A non-numeric entry was made.") 
       interest_prompt = False
    else:  
        if isdecimal == -1 :           # -1 says there wasn't a fraction entered
            if entered_interest_rate.isdigit():   # no fraction entered. so is it numeric?
                savings_rate = float(entered_interest_rate)  # it is, let's save it and move on
                interest_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")    
                interest_prompt = False
        else:
            b = entered_interest_rate.split(".")       # isolate whole from decimal numbers (remove .)
            c = b[0] + b[1]                          # Combine all numbers 
            if c.isdigit():                          #  Test if all numeric
                savings_rate =  float(entered_interest_rate)  # we're good to go
                interest_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")
                interest_prompt = False
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
            print(' ')
            print (f"Edit checks complete. Balance = ${savings_balance:.2f} ; Rate = {savings_rate / 100:.5f} ; Months = {savings_maturity} ")
            print(' ')
    else:
        month_prompt = False  
        print ("Invalid entry.  Must be numeric")  
    
    # Call the create_savings_account function and pass the variables from the user.
updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(f"The new savings balance including acrrued interest of ${interest_earned:.2f} is ${updated_savings_balance:.2f}. ")
print(" ")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
cd_balance = (float)
balance_prompt = False
interest_prompt = False
month_prompt = False
while balance_prompt == False:
    entered_savings_bal = input("Enter CD balance, in both dollars and cents '(Ex. $100.25 = 100.25)' - ..$")
    isdecimal = entered_savings_bal.find(".")   # check for cents entered
    how_many = entered_savings_bal.count('.')   # Get count of decimals
    if how_many > 1:
       print ("Invalid entry. A non-numeric entry was made.") 
       balance_prompt = False
    else: 
        if isdecimal == -1 :           # now check if cents was entered (no decimal?)
            print(f'Does not look as though any cents was entered.')
            balance_prompt = False    
        else:
            b = entered_savings_bal.split(".")       # isolate dollars and cents (remove .) 
            c = b[0]+b[1]                            # Combine dollars and cents without decimal
            if c.isdigit():                          #  Test if all numeric
                cd_balance = float(entered_savings_bal)
                balance_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")
                balance_prompt = False
while interest_prompt == False:
    print(f'Enter Interest "(APR)" rate as a whole number and fraction thereof.')
    entered_interest_rate = input("Ex. 5 1/4% : enter - 5.25; Ex for 6 7/8 : enter 6.875 ..%")
    isdecimal = entered_interest_rate.find(".")   # any fraction ? 
    how_many = entered_interest_rate.count('.')   # Get count of decimals
    if how_many > 1:
       print ("Invalid entry. A non-numeric entry was made.") 
       interest_prompt = False
    else:   
        if isdecimal == -1 :           # -1 says there wasn't a fraction entered
            if entered_interest_rate.isdigit():   # no fraction entered. so is it numeric?
                cd_rate = float(entered_interest_rate)  # it is, let's save it and move on
                interest_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")    
                interest_prompt = False
        else:
            b = entered_interest_rate.split(".")       # isolate whole from decimal numbers (remove .)
            c = b[0]+b[1]                            # Combine all numbers 
            if c.isdigit():                          #  Test if all numeric
                cd_rate =  float(entered_interest_rate)  # we're good to go
                interest_prompt = True
            else:
                print ("Invalid entry. A non-numeric entry was made.")
                interest_prompt = False
while month_prompt == False:
    entered_month = input("Enter term '(in months)' for CD...")
    if entered_month.isdigit():
        cd_maturity = int(entered_month)
        month_prompt = True
        if cd_maturity == 0 :
            month_prompt = False        
            print("Invalid month.  Must be greater than zero'(0)'") 
        else:
            month_prompt = True
            print(' ')
            print (f"Edit checks complete. Balance = ${cd_balance} ; Rate = {cd_rate / 100:.5f} ; Months = {cd_maturity} ")
            print(' ')
    else:
        month_prompt = False  
        print ("Invalid entry.  Must be numeric") 
    # Call the create_cd_account function and pass the variables from the user.
updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_rate, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print(' ')
print(f"At maturity, the balance including acrrued interest of ${interest_earned:.2f} is ${updated_cd_balance:.2f}. ")


if __name__ == "__main__":
    # Call the main function.
    main()