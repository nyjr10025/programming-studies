def solution(nums, target):
    if (len(nums) < 2 or len(nums) > 10**3 or target > 10**9 or target < -10**9): return []
    output = []
    for i, elem in enumerate(nums):
        if (elem > 10**9 or elem < -10**9): continue
        subtractVal = target - elem
        if (nums.count(subtractVal) == 0 or i == nums.index(subtractVal)): continue
        output = [i, nums.index(subtractVal)]
        break
    return output

n1 = [2,7,11,15]
t1 = 9 
s1 = [0,1]

n2 = [3,2,4]
t2 = 6
s2 = [1,2]

n3 = [3,3]
t3 = 6
s3 = [0,1]

def test(n, t, s):
    return f'Result: {solution(n, t)} | Solution: {s}'

print(test(n1, t1, s1))
print(test(n2, t2, s2))
print(test(n3, t3, s3))