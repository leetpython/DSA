class Solution:
    def subArraySum(self, arr, n, target):
        left = 0
        right = 1

        # window_sum is the sum of elements in arr[left..right]
        window_sum = arr[0]

        while right <= n:
            # If window_sum exceeds the target, then shrink the window from the left
            while (window_sum > target) and (left < right - 1):
                window_sum -= arr[left]
                left += 1

            # If window_sum is equal to the target
            if window_sum == target:
                # +1 to account for 1-based indexing
                return [left + 1, right]

            # Expand the window to the right (if possible)
            if right < n:
                window_sum += arr[right]
            right += 1

        # No such subarray exists
        return [-1]