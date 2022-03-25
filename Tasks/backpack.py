#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задача про рюкзак
"""

def backpack(capacity, weight, value, n):
    z = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                z[i][w] = 0
            elif weight[i - 1] <= w:
                z[i][w] = max(value[i - 1] + z[i - 1][w - weight[i - 1]], z[i - 1][w])
            else:
                z[i][w] = z[i - 1][w]
    return z[n][capacity]


if __name__ == "__main__":
    value = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    n = len(value)
    print("Максимальная цена рюкзака :", backpack(capacity, weight, value, n))
