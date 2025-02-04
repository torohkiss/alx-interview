#!/usr/bin/python3
"""Module to determine fewest number of coins needed to meet amount total"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
