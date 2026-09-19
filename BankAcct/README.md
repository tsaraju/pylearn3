Create a simplified banking application.

Create a BankAccount class containing account holder name, account number, and balance. 
Implement deposit(), withdraw(), check_balance(), and display_account_details(). 
Use a class variable for the bank name and a class method that can change the bank name for every account.

Add validation so that a user cannot withdraw more money than available.
Bonus: Keep track of the total number of bank accounts created.

Sample Input:
ac1 = acc("Raju", 2546532221566, 20000)
ac2 = acc("Rani", 2546532428569, 30000)
ac3 = acc("Rama", 2546532528007, 25000)

Sample Output:
Bank Account Details: 
Account holder name: Raju
Account number: 2546532221566
Total balance: 20000
Amount 10000 deposited, Total balance is 30000
Amount 1000 withdrawn, Total balance is 29000
Current Balance is : 29000
Bank Account Details: 
Account holder name: Rani
Account number: 2546532428569
Total balance: 30000
Amount 20000 deposited, Total balance is 50000
Amount 2000 withdrawn, Total balance is 48000
Current Balance is : 48000
Bank Account name :  ICICI
Bank Account Details: 
Account holder name: Rama
Account number: 2546532528007
Total balance: 25000
Amount 10000 deposited, Total balance is 35000
Amount 1000 withdrawn, Total balance is 34000
Current Balance is : 34000
Bank Account name :  YES
Total bank accounts:  3
