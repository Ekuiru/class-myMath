class myMath:

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def addition(self):
        self.result = self.a + self.b
        if self.result % 1 == 0:
            self.result = int(self.result)
        print('Сложение a и b:')                
        print('Ответ: ', self.result)

    def multiplication(self):
        self.result = self.a * self.b
        if self.result % 1 == 0:
            self.result = int(self.result)
        print('Умножение a на b:')
        print('Ответ: ', self.result)
    
    def division(self):
        if self.b != 0:
            self.result = self.a / self.b
            if self.result % 1 == 0:
                self.result = int(self.result)
            print('Деление a на b:')
            print('Ответ: ', self.result)
        else:
            print('Деление a на b:')
            print('Нет ответа')
    
    def subtraction(self):
        self.result = self.a - self.b
        if self.result % 1 == 0:
            self.result = int(self.result)
        print('Умножение a на b:')
        print('Ответ: ', self.result)
    
    def  pow(self):
        self.result = self.a ** self.b
        if self.result % 1 == 0:
            self.result = int(self.result)
        print('Возведение а в сетепень b:')
        print('Ответ: ', self.result)

    def sqrt(self):
        if self.a >= 0:
            self.result = self.a ** 0.5
            if self.result % 1 == 0:
                self.result = int(self.result)
            print('Корень a:')
            print('Ответ: ', self.result)
        else:
            print('Корень a:')
            print('Нет ответа')

num_1 = float(input())
num_2 = float(input())
m = myMath(num_1, num_2)
myMath.addition(m)
myMath.multiplication(m)
myMath.division(m)
myMath.pow(m)
myMath.sqrt(m)
