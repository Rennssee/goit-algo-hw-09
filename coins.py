import time


def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    coins_count = {}

    start_time = time.time()

    for coin in denominations:
        while amount >= coin:
            coins_count[coin] = coins_count.get(coin, 0) + 1
            amount -= coin

    execution_time = time.time() - start_time
    return coins_count, execution_time


def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 25, 50]
    coins_count = {}
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    start_time = time.time()

    for coin in denominations:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coins_count[i] = coin

    result_coins = {}
    while amount > 0:
        coin = coins_count[amount]
        result_coins[coin] = result_coins.get(coin, 0) + 1
        amount -= coin

    execution_time = time.time() - start_time
    return result_coins, execution_time


# Порівняння ефективності для різних сум:
amounts_to_test = [176, 533, 1954, 5734, 17634]
for amount in amounts_to_test:
    greedy_result, greedy_time = find_coins_greedy(amount)
    min_coins_result, min_coins_time = find_min_coins(amount)

    print(f"\nAmount: {amount}")
    print("Greedy Algorithm Result:", greedy_result)
    print("Greedy Algorithm Time:", greedy_time)
    print("Dynamic Programming Result:", min_coins_result)
    print("Dynamic Programming Time:", min_coins_time)
