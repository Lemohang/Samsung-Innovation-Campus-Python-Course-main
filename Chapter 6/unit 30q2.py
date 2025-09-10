def coin_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    
    return change if amount == 0 else None


coins = list(map(int, input("Input the coins: ").split()))
coins.sort(reverse=True)
print(coins)
amount = int(input("Input the amount: "))
changes = coin_change(coins, amount)


print(changes, len(changes)) if changes else print("Eish! Not enough coins to make the amount.")