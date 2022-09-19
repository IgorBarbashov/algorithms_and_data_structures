# Реализация RSQ (range sum query) через префиксные суммы

def makePrefixSum(nums):
    prefixSum = [0] * (len(nums) + 1)
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
    return prefixSum

def rsq(prefixSum, l, r):
    return prefixSum[r] - prefixSum[l]
