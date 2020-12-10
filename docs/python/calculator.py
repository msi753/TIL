class Calculator():

    def __init__(self, numList):
        self.numList = numList

    def sum(self):
        result = 0
        for i in self.numList:
            result += i
        return result

    def avg(self):
        total = self.sum()
        return total / len(self.numList)

if __name__ == "__main__":
    cal1 = Calculator([1, 2, 3, 4, 5])
    print(cal1.sum())
    print(cal1.avg())


# 모듈 사용
# py
# import calculator
# c = calculator.Calculator()
# c = calculator.Calculator([1, 2, 3])
# c.sum()
# c.avg()