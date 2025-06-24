class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        found_keys = [i for i in nums if i != key and i != k]
        print(sorted(found_keys))

test = Solution()
test.findKDistantIndices([3,4,9,1,3,9,5],9,1)
        