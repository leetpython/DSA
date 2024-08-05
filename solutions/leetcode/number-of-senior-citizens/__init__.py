from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        phone = detail[0:10]
        gender = detail[10:11]
        age = detail[11:13]
        seat = detail[13:15]
        """

        counter = 0

        for person_detail in details:
            age = int(person_detail[11:13])
            if age > 60:
                counter += 1

        return counter
