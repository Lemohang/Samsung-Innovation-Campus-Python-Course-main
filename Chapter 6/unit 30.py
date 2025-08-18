def coin_change(change, coins):
    result = {}
    coins_keys = sorted(coins.keys(), reverse=True)

    for coin in coins_keys:
        coins_counter = min(change // coin, coins[coin])
        change -= coins_counter * coin
        coins[coin] -= coins_counter

        if coins_counter:
            result[coin] = coins_counter

    return result, change



coins = {}

num_of_coins = int(input("How many different coin types do you have? "))

for i in range(num_of_coins):
    coin_value = int(input("Enter coin value #{}: ".format(i+1)))
    coin_count = int(input("Enter how many {}-coins you have: ".format(coin_value)))
    coins[coin_value] = coin_count

amount = int(input("\nEnter the amount you need change for: "))

print("\n=== Welcome to Monate Wholesale ===")
print("\n==== Coin BEFORE ====")
for coin, count in sorted(coins.items(), reverse=True):
    print("{}: {}".format(coin, count))


result, leftover = coin_change(amount, coins)

print("\n=== Result ===")
print("Coins used: {}".format(result))
if leftover > 0:
    print("Could not make full change. Leftover: {}".format(leftover))
else:
    print("Change fully made!")


print("\n--- Coin Inventory AFTER ---")
for coin, count in sorted(coins.items(), reverse=True):
    print("{}: {}".format(coin, count))
