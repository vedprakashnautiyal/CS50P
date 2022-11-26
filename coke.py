print("Amount Due: 50")
amount=50
change=0
coin=int(input("Insert Coin: "))

while(True):
        if (coin==5 or coin==10 or coin==25):
                amount=amount-coin
                change=change + coin
                if (change-50<0):
                    print (f"Amount Due: {amount}")
                if (change-50>=0):
                    print("Change Owed: ",change-50)
                    exit(0)
                else:
                    # print (f"Amount Due: {amount}")
                    coin=int(input("Insert Coin: "))
                    continue
        else:
            print (f"Amount Due: {amount}")
            coin=int(input("Insert Coin: "))
            continue

