class Solution:
    def isAnagram(self, s, t):
        #Если длины разные, строки не могут быть анаграммами
        if len(s)!=len(t):
            return False

        count={}

        #Подсчитываем символы первой строки
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1

        #Уменьшаем счётчики по символам второй строки
        for ch in t:
            if ch not in count:
                return False

            count[ch]-=1

            if count[ch]<0:
                return False

        #Проверяем, что все счётчики стали нулевыми
        for value in count.values():
            if value!=0:
                return False

        return True