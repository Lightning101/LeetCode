
def twoSum( nums, target):
    size = len(nums)
    sorted_list = [[j, i] for i, j in enumerate(nums)]
    sorted_list.sort(key=lambda e: e[0])
    p1, p2 = 0, size - 1
    while p1 != p2:
        v1 = sorted_list[p1]
        v2 = sorted_list[p2]
        sum = v1[0] + v2[0]
        if target < sum :
            p1 += 1
        elif target >sum:
            p2 -= 1
        else:
            return [v1[1], v2[1]]
    return []

nums = [2,7,11,15]

print(twoSum(nums,9))