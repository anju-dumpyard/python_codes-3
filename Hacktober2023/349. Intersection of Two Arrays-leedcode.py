Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=set(nums1)

        y=set(nums2)

        return list(x.intersection(y))