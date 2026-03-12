class MinStack:

    def __init__(self):
        # основной стек
        self.st=[]
        # стек минимумов
        self.mn=[]

    def push(self, val: int) -> None:
        self.st.append(val)

        # если стек минимумов пуст или новый элемент меньше/равен текущему минимуму
        if not self.mn or val<=self.mn[-1]:
            self.mn.append(val)

    def pop(self) -> None:
        x=self.st.pop()

        # если удаляем текущий минимум, убираем и из стека минимумов
        if x==self.mn[-1]:
            self.mn.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn[-1]