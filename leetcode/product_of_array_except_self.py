from typing import List
from collections import deque
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product(a: int, b: int):
            return a*b
        product_list = []
        prefix_product = 1
        for idx in range(len(nums)):
            suffix_list = nums[idx + 1:]
            if len(suffix_list) == 0:
                productNum = nums[idx]
            else:
                productNum = reduce(product, suffix_list)
            product_list.append(productNum)
        return product_list

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
print(sol.productExceptSelf([-1,1,0,-3,3]))
# print(sol.productExceptSelf())
# print(sol.productExceptSelf())
        