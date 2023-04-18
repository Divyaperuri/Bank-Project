

balance=0
customername=['naresh','kumar']
customerpin=['1234','2345']
customerbalance=[231,23421]
while True:
    print("*"*10,'welcome to naresh bank',"*"*10)
    print('''which function you want to use from below
    1) open new account
    2) withdrawl
    3) deposit
    4) check balance
    5) exit''')
    option=int(input('enter the number which you want to select: '))
    if option==1:
        noc=eval(input('number of customers'))
        if noc>5:
            print("the number of registration exceeded the max regidtratiom")
        else:
            for i in range(noc):
                name=input('enter your name: ')
                customername.append(name) 
                pin=int(input('enter the pin you want to put: '))
                customerpin.append(pin)
                deposit=eval(input("enter the amount you want to deposit: "))
                balance+=deposit
                customerbalance.append(balance)
                print("\n")
                if name in customername:
                    ind=customername.index(name)
                    print("name =",customername[ind])
                    print("pin =",customerpin[ind])
                    print("balance =",customerbalance[ind])
                    print("\n")
                    print("your name,pin,balance has updated")
                    print("\n")
                    print("&"*10,'new account successfully created',"&"*10)
                    print("Note! Please remember the Name and Pin\n")
                    print(customername,customerpin)
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...") 
    elif option==2:
        j=0
        while j<1:
            name=input('enter your name')
            pin=input('enter your pin')
            k=-1
            while k<len(customername)-1:
                k=k+1
                if name==customername[k]:
                    if pin==customerpin[k]:
                        j=j+1
                    #     print('login')
                    # else:
                    #     print('not')
                    print("your balance is ",customerbalance[k])
                    balance=customerbalance[k]
                    amo=int(input('enter the amount you want to withdrawl'))
                    if amo>customerbalance[k]:
                        print("insufficient balance")
                    else:
                        balance=balance-amo
                        customerbalance[k]=balance
                        print('your updated balace is',customerbalance[k])
                else:
                    print('invalid login')
    elif option==3:
        j=0
        while j<1:
            name=input('enter your name')
            pin=eval(input('enter your pin'))
            j+=1
            k=-1
            if k<len(customername[k])-1:
                k+=1
                if name==customername[k]:
                    if pin==customerpin[k]:
                        print('your current balance is: ',customerbalance[k])
                        balance=customerbalance[k]
                        dep=int(input('enetr the amount you want to deposit'))
                        balance=balance+dep
                        customerbalance[k]=balance
                        print("your updated balance is :",customerbalance[k])
                else:
                    print('inavlid login')
    elif option==4:
        j=0
        while j<1:
            name=input('enter your name')
            pin=int(input('enter your pin'))
            j+=1
            k=-1
            if k<len(customername[k])-1:
                
                if name==customername[k]:
                    if pin==customerpin[k]:
                        print("your balance is: ",customerbalance[k])
                        k+=1
                else:
                    print('invalid login')

    elif option==5:
        print("thank you visit again")
        print("bye bye")
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
        mainMenu=input("enter the button enter to go back to the main menu")



                    

            # for i in range(-1,len(customername)-1):
            #     if name==customername[i]:
            #         if pin==customerpin[i]:
            #             print('login success')
            #     else:
            #         print('invalid')
            #         j=j+1
            
            


