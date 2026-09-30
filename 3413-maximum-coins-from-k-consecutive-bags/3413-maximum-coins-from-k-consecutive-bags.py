from bisect import bisect_right

class Solution(object):
    def maximumCoins(self, coins, k):
        coins.sort()

        n = len(coins)

        starts = []
        prefix = [0]

        for l, r, c in coins:
            starts.append(l)
            prefix.append(
                prefix[-1] + (r - l + 1) * c
            )

        def coins_until(x):
            idx = bisect_right(starts, x) - 1

            if idx < 0:
                return 0

            l, r, c = coins[idx]

            total = prefix[idx]

            if x >= r:
                total += (r - l + 1) * c
            else:
                total += (x - l + 1) * c

            return total

        max_val = 0

        for l, r, c in coins:
            start = l

            cur = (
                coins_until(start + k - 1)
                - coins_until(start - 1)
            )

            max_val = max(max_val, cur)

            start = r - k + 1

            cur = (
                coins_until(start + k - 1)
                - coins_until(start - 1)
            )

            max_val = max(max_val, cur)

        return max_val