class Solution:
    def groupAnagrams(self, strs):
        # Словарь: отсортированное слово -> список анаграмм
        groups = {}

        for word in strs:
            # Получаем ключ, общий для всех анаграмм
            key = ''.join(sorted(word))

            # Если такого ключа ещё нет, создаём пустой список
            if key not in groups:
                groups[key] = []

            # Добавляем слово в нужную группу
            groups[key].append(word)

        return list(groups.values())