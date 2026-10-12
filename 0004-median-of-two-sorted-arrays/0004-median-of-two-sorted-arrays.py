class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2,nums1
        n = len(nums1)
        m = len(nums2)
        low = 0
        high  = len(nums1)
        while low <= high:
            mid1 = (low + high)//2
            mid2 =  (n+m+1)//2-mid1
            if mid1 == 0:
                l1 = float("-inf")
            else:
                l1=nums1[mid1-1]
            if mid1 == n:
                r1 = float("inf")
            else:
                r1 = nums1[mid1]
            if mid2 == 0:
                l2 = float("-inf")
            else:
                l2=nums2[mid2-1]
            if mid2 == m:
                r2 = float("inf")
            else:
                r2 = nums2[mid2]
            if l1 <= r2 and l2 <= r1:
                if (n+m)%2 ==1:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0


       

  
        