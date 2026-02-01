class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target)) 
