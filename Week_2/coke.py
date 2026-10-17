def VerifCoin(coin):
    return int(coin) in [25, 10, 5]


amount = 50

while amount > 0:
    print("Amount Due:", amount)
    coin = input("Insert Coin: ")

    if VerifCoin(coin):
        amount -= int(coin)

print("Change Owed:", abs(amount))