class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        down = False
        up = False
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]: return False
            if arr[i-1] > arr[i]: down = True
            if arr[i-1] < arr[i]: 
                up = True
                if down: return False
        if up and down: return True
        return False