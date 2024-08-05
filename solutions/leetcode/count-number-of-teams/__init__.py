from typing import List

# TODO: Look into using Fenwick trees for O(N*log(maxRating)) performance


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)

        teams = 0

        for mid in range(N):
            # count(indices less than `mid` where the rating < rating[mid])
            lt = 0
            for i in range(0, mid):
                if rating[i] < rating[mid]:
                    lt += 1

            # count(indices greater than `mid` where the rating > rating[mid])
            gt = 0
            for i in range(mid + 1, N):
                if rating[mid] < rating[i]:
                    gt += 1

            # Number of teams (ascending)
            # for rating[i] < rating[j] < rating[k]
            teams += lt * gt

            # Number of teams (descending)
            # for rating[k] < rating[j] < rating[i]
            to_left = mid
            to_right = N - 1 - to_left
            teams += (to_left - lt) * (to_right - gt)

        return teams
