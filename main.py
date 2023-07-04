def knapsack_subset(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    subset = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append((weights[i - 1], values[i - 1]))
            j -= weights[i - 1]
        i -= 1

    return subset

# Given data
weights = [3, 2, 4, 1]
values = [105, 20, 60, 40]
capacity = 5

subset = knapsack_subset(weights, values, capacity)
total_value = sum(value for weight, value in subset)

print("Subset of items that fit into the knapsack:")
for weight, value in subset:
    print(f"Item with weight {weight} kg and value Ksh. {value}")

print("Total value:", total_value)

