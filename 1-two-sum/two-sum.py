class Solution:
    def twoSum(self, nums, target):
        #Словарь:число -> индекс
        seen = {}

        for i in range(len(nums)):
            need=target-nums[i]

            #Если нужное число уже встречалось, возвращаем ответ
            if need in seen:
                return [seen[need],i]

            #Сохраняем текущее число и его индекс
            seen[nums[i]]=i