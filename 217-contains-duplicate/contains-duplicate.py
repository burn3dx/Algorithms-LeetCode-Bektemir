class Solution:
    def containsDuplicate(self, nums):
        # Множество для уже встреченных элементов
        seen=set()

        for num in nums:
            #Если число уже есть в множестве, найден дубликат
            if num in seen:
                return True

            #Иначе добавляем число в множество
            seen.add(num)

        return False