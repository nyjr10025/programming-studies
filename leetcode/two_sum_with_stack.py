from collections import deque
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        returnList = deque(maxlen=2)
        for idx, elem in enumerate(nums):
            # add idx to return list
            returnList.append(idx)
            # check if its last, if so its pro
            if idx == len(nums) -1:
                returnList.append(idx)
                return returnList
            restOfList = deque(nums[idx+1:])
            while len(restOfList) > 0:
                if target - elem == restOfList[-1]:
                    returnList.append(idx + len(restOfList))
                    return returnList
                restOfList.pop()
            returnList.pop()