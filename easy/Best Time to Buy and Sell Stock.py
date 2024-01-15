def maxProfit(prices) -> int:
    # O(1) space
    # O (n) time
    if len(prices) == 1:
        return 0
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        max_profit = max(max_profit, prices[right]-prices[left])
        if prices[right] < prices[left]:
            left = right
        right += 1
    return max_profit



assert maxProfit([3,2,1]) == 0
assert maxProfit([3,2,4]) == 2
assert maxProfit([3,2,2]) == 0
assert maxProfit([1,2,3]) == 2
assert maxProfit([7,1,5,3,6,4]) == 5


