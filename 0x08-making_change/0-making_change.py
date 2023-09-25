#!/usr/bin/python3
"""Making Change Algorithm"""


def makeChange(coins, total):
    """
        This function returns the:
            Minimum number of coin needed to meet a given value
            Fewest number of coins needed to meet total
        Args:
            coins (list of ints): a list of coins
            total (int): total/value to be met with the given coins

    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    The value of a coin will always be an integer greater than 0
    You can assume you have an infinite number of each
    denomination of coin in the list
    Your solution’s runtime will be evaluated in this task
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count

    # if total < 0:
    #     return 0  # If total is negative, return 0.

    # # Create a list to store the minimum number of coins
    # needed for each total from 0 to 'total'.
    # # Initialize all values with a large number to start.
    # dp = [float('inf')] * (total + 1)

    # # The minimum number of coins needed to make change for 0 is 0.
    # dp[0] = 0

    # # Iterate through each coin denomination and update the dp list.
    # for coin in coins:
    #     for amount in range(coin, total + 1):
    #         dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # # If dp[total] is still 'inf', it means no combination
    # of coins can make the total.
    # return dp[total] if dp[total] != float('inf') else -1
