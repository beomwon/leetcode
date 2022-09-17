class Solution:
    def merge(self, nums1, m, nums2, n):
        for i,v in enumerate(sorted(nums1[:m] + nums2[:n])): nums1[i] = v
        