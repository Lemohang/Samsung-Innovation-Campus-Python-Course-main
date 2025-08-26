counter = 0

def find_heavy_coin(coins):
    global counter
    counter += 1
    if len(coins) == 1:
        return coins[0]
    if len(coins) == 2:
        if coins[0]["weight"] > coins[1]["weight"]:
            return coins[0]
        else:
            return coins[1]
    mid = len(coins) // 2
    left, right = coins[:mid], coins[mid:]
    left_w = sum(c["weight"] for c in left)
    right_w = sum(c["weight"] for c in right)
    if left_w > right_w:
        return find_heavy_coin(left)
    else:
        return find_heavy_coin(right)

coins = [
    {"coin": 1, "weight": 100}, {"coin": 2, "weight": 100},
    {"coin": 3, "weight": 100}, {"coin": 4, "weight": 100},
    {"coin": 5, "weight": 100}, {"coin": 6, "weight": 100},
    {"coin": 7, "weight": 100}, {"coin": 8, "weight": 111}
]

print("Heaviest coin:", find_heavy_coin(coins))
print("Number of executions:", counter)
