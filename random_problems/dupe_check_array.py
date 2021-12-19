# The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time where the integer values are smaller than the length of the array!

# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm can detect that there are a duplicate with value 1.

# Note: the array can not contain items smaller than 0 and items with values greater than the size of the list. This is how we can achieve O(N) linear running time complexity!

def solution(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
            continue
        # else:
        print(f'Repetition found {str(abs(num))}')



if __name__ == '__main__':
    dupe_array = [1, 2, 3, 1, 5]
    solution(dupe_array)
# Repetition found 1
# Traceback (most recent call last):
#   File "/Users/nyjr/projects/InterviewPrep/dupe_check_array.py", line 19, in <module>
#     solution(dupe_array)
#   File "/Users/nyjr/projects/InterviewPrep/dupe_check_array.py", line 9, in solution
#     if nums[abs(num)] >= 0:
# IndexError: list index out of range

