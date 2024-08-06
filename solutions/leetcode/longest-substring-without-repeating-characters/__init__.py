from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)

        # Maps a character of the window to its position in the string
        # (default -1)
        position_map = defaultdict(lambda: -1)

        window_start = 0
        longest_substr_len = 0
        for i in range(N):
            char = s[i]

            # If this character already exists within the window at some position
            if position_map[char] >= window_start:
                # Make the window start from the character after this position
                window_start = position_map[char] + 1

            position_map[char] = i

            # At this point, the window is guaranteed to have no repeating characters
            window_len = i - window_start + 1
            longest_substr_len = max(longest_substr_len, window_len)

        return longest_substr_len
