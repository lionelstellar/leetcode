class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i1 , i2 = 0, 0
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 == len(nums1):
                nums.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2):
                nums.append(nums1[i1])
                i1 += 1
            else:
                elem1 = nums1[i1]
                elem2 = nums2[i2]
                if elem1 > elem2:
                    nums.append(elem2)
                    i2 += 1
                else:
                    nums.append(elem1)
                    i1 += 1
        #print(nums)
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1] + nums[len(nums)//2])/2

s = Solution()
print(s.findMedianSortedArrays([1,2],[]))