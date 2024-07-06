Customers=['Nadh','Badhri','Ramya','Cherry','LLohith']
CustomersPassword=['123','345','456','678','890']
CustomersBalance=[123,456,23,89,567]

deposition=0
withdraw=0
Balance=0
c1=1
c2=5
i=0
from datetime import datetime

while True:
    print(40*'=')
    print(40*'*')
    print(10*'-'+'Welcome to Times Bank'+8*"-")
    print(40*'*')
    print("=<>=   1. Create new Bank account   =<>=")
    print("=<>=   2. Withdraw ammount          =<>=")
    print("=<>=   3. Deposit amount            =<>=")    
    print("=<>=   4. Check Customers & Balance =<>=")
    print("=<>=   5. Bank statement            =<>=")   
    print("=<>=   6. Exit/quit                 =<>=")
    print(40*'*')
    print(40*'=')


    CustomerInput=int(input('Select your choice from above:'))
    if CustomerInput==1:
        print("Choice number 1 is selected by the customer")
        NOC=int(input('\nEnter no.of accounts you want to create:'))
        if NOC>5:
            print("\nSorry a person can create maximum of 5 accounts at a time\n")
            NOC=NOC-NOC
        else:
            while NOC>i:
                Customer_name=str(input("Enter name:"))
                Customer_password=input('Enter pin:')
                Customer_deposit=float(input('Enter initial deposit:'))
                Customers.append(Customer_name)    
                CustomersPassword.append(Customer_password)
                CustomersBalance.append(Customer_deposit)
                print(10*'-')
                print(10*'*')
                print('Name:',end=" ")
                print(Customers[c2])
                print('Balance:',end=" ")   
                print(CustomersBalance[c2])
                print('Pin:',end=" ")
                print(CustomersPassword[c2]) 
                print(10*'-')
                print(10*'*')
                NOC=NOC-1
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif CustomerInput==2:
        print("Choice number 2 is selected by the customer")
        j=0
        while j < 1:
            k = -1
            name = input("Please Enter name : ")
            pin = input("Please Enter pin : ")
            while k < len(Customers) - 1:
                k = k + 1
                if name == Customers[k]:
                    if pin == CustomersPassword[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(CustomersBalance[k], end=" ")
                        print("-/Rs\n")
                        Balance = (CustomersBalance[k])
                        withdraw = eval(input("Input value to Withdraw : "))
                        if withdraw > Balance:
                            deposition=eval(input("Withdrawal amount is greater than Account balance add some balance to it"))
                            Balance=deposition+Balance
                            print("Your Current Balance:", end=" ")
                            print(Balance, end=" ")
                            print("-/Rs\n") 
                            Balance = Balance - withdraw
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            CustomersBalance[k] = Balance
                            print("Your New Balance: ", Balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            Balance=Balance-withdraw
                            print('\n')
                            print("------Withdraw Successfull------")
                            CustomersBalance[k]=Balance
                            print("Ava Bal:",Balance,end=" ")
                            print("-/Rs\n")
                            print(10*'-')
                            print("Your New Balance: ", Balance, end=" ")
                            print("-/Rs\n\n")
        if j<1:
            print('Invalid details')
            break                
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif CustomerInput==3:
        print("Choice number 3 is selected by the customer")
        n=0
        while n<1:
            k=-1
            name=input('Enter name:')
            passw=input('Enter pin:')
            while k<len(Customers)-1:
                k=k+1
                if name==Customers[k]:
                    if passw==CustomersPassword[k]:
                        print('Available Balance:',CustomersBalance[k],end=" "+'\n')
                        deposition=eval(input('Enter amount to deposit:'))
                        Balance=CustomersBalance[k]
                        Balance=Balance+deposition
                        CustomersBalance[k]=Balance

                        print(15*'-')
                        print('Deposited successfully!!'+'\n')
                        print('Name:',Customers[k],end=" "+'\n')
                        print('New Balance:',CustomersBalance[k],end=" "+'\n')
                        n=n+1
                        print(15*'-')
                        print('\n\n')
                        break
                else:
                    print('Invalid Details!!')
                    break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif CustomerInput==4:
        print("Choice number 4 is selected by the customer")
        print("Customers:\n")
        print(Customers)
        print('\n')
        print('Account Balances:\n')
        print(CustomersBalance)    
        print('\n')
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif CustomerInput==5:
        n=0
        while n<1:
            k=-1
            name=input('Enter name:')
            pin = input('Enter pin:')
            print('\n')
            while k<len(Customers)-1:
                k=k+1
                if name==Customers[k]:
                    if pin==CustomersPassword[k]:
                        print(45*"*")
                        print(15*"-"+'Times Bank'+20*"-")
                        print(45*"*")
                        print("Date and Time:  ",datetime.now())
                        print(45*'-')
                        print("Name:      "+10*" ",Customers[k])
                        print("Ac Balance:"+10*" ",CustomersBalance[k],'-Rs\-')
                        print("Pin:       ",10*" ",CustomersPassword[k])
                        print(45*"*"+'\n')
                        n=n+1
                        break
                else:
                    print("Invalid details!!")    
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")            


    elif CustomerInput==6:
        print("Choice number 6 is selected by the customer")
        print('| Thankyou for visiting!! |')
        print("\n| Visit again |")
        print('\n| Bye bye |')
        break
    else:
        print('\nInvalid options please try again\n')