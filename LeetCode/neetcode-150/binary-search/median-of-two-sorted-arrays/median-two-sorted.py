from typing import List
class Solution:
    def findLowerMedian(self, nums1, nums2):
        #checks if nums1 contains lower median of combined list nums1 + nums2
        l1, r1 = 0, len(nums1)
        l2, r2 = 0, len(nums2)
        need = (len(nums1) + len(nums2) - 1) // 2
        med1 = None
        while not med1 and l1 < r1:
            mid1 = (l1 + r1) // 2
            l2, r2 = 0, len(nums2)
            while l2 < r2:
                mid2 = (l2 + r2) // 2
                if nums1[mid1] > nums2[-1]:
                    below = mid1 + mid2
                else:

                print(nums1[mid1], nums2[mid2], mid1, mid2, below)
                if nums2[mid2] >= nums1[mid1]:
                    #below += nums2[mid2] == nums1[mid1]
                    if below < need:
                        l2 = mid2 + 1
                    elif below > need:
                        r2 = mid2
                    elif mid2 == 0 or nums2[mid2 - 1] <= nums1[mid1]:
                        med1 = nums1[mid1]
                        break   
                    else:
                        break
                else:
                    l2 = mid2 + 1
            if nums1[mid1] >= nums2[-1] or  mid1 >= need:
                r1 = mid1
            else:
                l1 = mid1 + 1

        print(med1)
        return med1

    def findUpperMedian(self, nums1, nums2):
        #checks if nums1 contains upper median of combined list nums1 + nums2
        l1, r1 = 0, len(nums1)
        need = (len(nums1) + len(nums2) - 1) // 2
        med2 = None
        while not med2 and l1 < r1:
            mid1 = (l1 + r1) // 2
            l2, r2 = 0, len(nums2)
            while l2 < r2:
                mid2 = (l2 + r2) // 2
                above = (len(nums1) - mid1) + (len(nums2) - mid2) - 2
                print(nums1[mid1], nums2[mid2], mid1, mid2, above)
                if nums2[mid2] <= nums1[mid1]:
                    #above += nums2[mid2] == nums1[mid1]
                    if above < need:
                        r2 = mid2
                    elif above > need:
                        l2 = mid2 + 1
                    elif mid2 == len(nums2) - 1 or nums2[mid2 + 1] >= nums1[mid1]:
                        med2 = nums1[mid1]
                        break   
                    else:
                        break
                else:
                    r2 = mid2

            if nums1[mid1] <= nums2[0] or len(nums1) - mid1 - 1 >= need:
                l1 = mid1 + 1
            else:
                r1 = mid1

        print(med2)
        return med2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            middle = (len(nums2) - 1) // 2
            if len(nums2) % 2 == 0:
                return (nums2[middle] + nums2[middle + 1]) / 2
            else:
                return nums2[middle]
                
        if len(nums2) == 0:
            middle = (len(nums1) - 1) // 2
            if len(nums1) % 2 == 0:
                return (nums1[middle] + nums1[middle + 1]) / 2
            else:
                return nums1[middle]

        med1 = self.findLowerMedian(nums1, nums2) or self.findLowerMedian(nums2, nums1)

        if (len(nums1) + len(nums2)) % 2 != 0:
            return med1

        med2 = self.findUpperMedian(nums1, nums2) or self.findUpperMedian(nums2, nums1)

        return (med1 + med2) / 2

sol = Solution()
find = sol.findMedianSortedArrays
args = [1,2,3,4,5,], [6,7,8,9,10,11,12,13,14,15,16,17]
find(*args)
