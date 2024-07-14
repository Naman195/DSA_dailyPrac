nums = [1,2,3, 1]

def containsDup(nums):
    n = len(nums)
    mp = {}
    for i in range(n):
        mp[nums[i]] = mp.get(nums[i], 0) + 1
    for k, v in mp.items():
        if v > 1:
            return True
    return False
print(containsDup(nums))