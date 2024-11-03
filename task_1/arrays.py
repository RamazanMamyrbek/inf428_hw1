class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0: return

        left = m - 1
        right = n - 1
        idx_end = len(nums1) - 1

        while left >= 0 and right >= 0:
            if nums1[left] < nums2[right]:
                nums1[idx_end] = nums2[right]
                right -= 1
            else:
                nums1[idx_end] = nums1[left]
                left -= 1
            idx_end -= 1

        while left >= 0:
            nums1[idx_end] = nums1[left]
            idx_end -= 1
            left -= 1

        while right >= 0:
            nums1[idx_end] = nums2[right]
            idx_end -= 1
            right -= 1
