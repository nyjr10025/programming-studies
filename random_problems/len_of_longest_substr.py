from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0 or len(s) > 5*10**4:
        return 0
    output = deque([])
    for ind, letter in enumerate(s):
        if ind == 0:
            output.append(letter)
            continue
        # if s[ind - 1] == letter:
        #     continue
        if letter in ''.join(output):
            if s[ind - 1] == letter:
                continue
            if s[0] == letter:
                output.popleft()
                # continue
        output.append(letter)
        if ''.join(output) not in s:
            output.popleft()
    print(''.join(output))
    if sum([1 for letter in output if output.count(letter) == 1]) == len(output):
        
    return len(output)


str1 = "abcabcbb"
sol1 = 3

str2 = "dvdf"
sol2 = 3

str3 = "pwwkew"
sol3 = 3


def test(string, solution):
    return f'Result: {lengthOfLongestSubstring(string)} | Solution: {solution}'


print(test(str1,  sol1))
print(test(str2,  sol2))
print(test(str3,  sol3))
