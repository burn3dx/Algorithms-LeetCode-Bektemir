class MyQueue:

    def __init__(self):
        # первый стек для добавления
        self.s1=[]
        # второй стек для извлечения
        self.s2=[]

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # если второй стек пуст, переносим элементы из первого
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1)==0 and len(self.s2)==0