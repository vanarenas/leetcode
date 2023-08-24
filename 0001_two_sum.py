class Solution:

    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target

        index = []

        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    index.extend([i,j])

        return index


# ----- TEST CASE ----- #
nums = [2,7,11,15]
target = 9
index = Solution()
print(index.twoSum(nums, target))
