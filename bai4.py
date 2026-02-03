class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1


# ---- MAIN ----
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([0, 0], [0, 0]),
        ([], [1]),
        ([2], [])
    ]

    for a, b in tests:
        print(f"nums1 = {a}, nums2 = {b}")
        print("Median =", sol.findMedianSortedArrays(a, b))
        print("-" * 30)
