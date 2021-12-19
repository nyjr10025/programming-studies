from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkDict = {}
        for num in nums:
            if num in checkDict:
                return True
            checkDict[num] = num
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
