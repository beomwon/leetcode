class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = sorted(nums1 + nums2)
        length = len(answer)/2
        if length == int(length):
            return (answer[int(length)] + answer[int(length-1)])/2
        else:
            return answer[int(length)]
            