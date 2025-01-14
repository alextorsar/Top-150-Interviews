from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m or j < n:
            if i < m:
                if j < n:
                    if nums1[i] < nums2[j]:
                        i+=1
                    else:
                        for aux in range(m,i,-1):
                            nums1[aux] = nums1[aux - 1]
                        nums1[i] = nums2[j]
                        i+=1
                        j+=1
                        m+=1
                else:
                    i = m
            else:
                for j in range(j,n):
                    nums1[i] = nums2[j]
                    i+=1
                j = n    