class Solution:
    def intersection(self, nums1, nums2):
        # Множество элементов первого массива
        set1 = set(nums1)

        # Множество для результата
        result = set()

        for num in nums2:
            # Если элемент есть в первом множестве, добавляем его в результат
            if num in set1:
                result.add(num)

        return list(result)