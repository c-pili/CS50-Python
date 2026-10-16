amount = 50

while(amount > 0):
    print("Amount Due: ", amount)
    coin = input("Insert Coin: ")
    bool = VerifCoin(coin)
    if(bool == True):
        amount -= coin
    else:
        print("Invalid Coin")



def VerifCoin(n):
    if((n == 25) or (n == 10) or (n == 5)):
        return True
    else:
        return False