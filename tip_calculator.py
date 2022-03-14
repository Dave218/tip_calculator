def repeat(): # This functions enables the user to start over

    print('Welcome to the tip calculator!\n')

    # The variable 'bill' asks for the bill from the user
    while True:
        try:
            bill = float(input("What was the total bill? \n$"))
            break
        except ValueError:
            print('Please enter a numerical value. Try again.') 
   
    tax = bill * 0.10 # calculates the taxes
    subtotal = bill + tax # subtotal before tip

    # Asking the user if they want to add a tip. And if the user inputs a string by mistake. They get the option to try again.
    while True:
        try:
            tip = int(input("How much of a tip would you like to give? Enter the amount only, please do not include a % sign. \n%"))
            break
        except ValueError:
            print('Please enter a numerical value. Try again.') 


    # Asking the user if they want to add another tip
    while True:
        try:
            tip_2  = int(input("Would you like to give an additional tip? Enter the amount only, please do not include a % sign. \n%"))
            tip_total = tip_2 + tip
            total_bill = tip_total/100 * bill + subtotal # This calculates the total amount including tip.
            break
        except ValueError:
            total_bill = tip/100 * bill + subtotal # If the user doesn't add a tip, this calculates the original tip.
            break


    while True:
        try:
            people = int(input("How many are splitting the bill? \n"))
            break
        except ValueError:
            print('Please enter a numerical value. Try again.') 
    


    total_amount_due = total_bill # Calling another variable to take the 'total_bill' and convert it to a string, so the output would allow 2 decimal places. 
    amount_due = "{:,.2f}".format(total_amount_due) # This converts 'total_bill' to a string

    splitting_the_bill = total_bill / people # This variable gives us how much each person needs to pay.

    final_amount = "{:,.2f}".format(splitting_the_bill) # # This converts 'splitting_the_bill' to a string so the output would allow 2 decimal places. 

    print(f'The total cost of your order is ${amount_due}. Each customer should pay ${final_amount}. \nThank you for your business!\n')

    # In case the user wants to start over
    check = input("Made a mistake? Want to make a change? To start over enter a 'Y'. Or anything else to exit the program. ")
    if check.upper() == "Y": # loop back to the start
         repeat()
    else:
         print('Thank you, and have a wonderful day!')
    exit() #exits the program

repeat()
