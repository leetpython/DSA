from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Map every string to its frequency
        freq = {}
        for string in arr:
            if not string in freq:
                freq[string] = 0
            freq[string] += 1

        # Count the distinct strings
        counter = 0
        for string in arr:
            # If string is distinct
            if freq[string] == 1:
                counter += 1

                if counter == k:
                    return string

        # There are fewer than k distinct strings
        return ""
