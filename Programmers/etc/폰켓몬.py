def solution(nums):
    answer = 0
    cnt = len(nums) // 2
    nums = list(set(nums))
    
    if len(nums) >= cnt:
        return cnt
    else:
        return len(nums)