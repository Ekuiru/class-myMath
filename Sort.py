class Sort:

    def __init__(self, N, spisok):
        self.N = N
        self.buff = 0
        self.spisok = spisok


    def list(self):
        for i in range(self.N):
            print('Введите элемент списка: ')
            self.spisok.append(int(input()))
        print('Неотсортированный список: ')
        print(self.spisok)
 
    def bubble(self):
        for i in range(self.N - 1):
            for j in range(self.N-i-1):
                if self.spisok[j] > self.spisok[j+1]:
                    self.buff = self.spisok[j]
                    self.spisok[j] = self.spisok[j+1]
                    self.spisok[j+1] = self.buff
        print('Список отсортирован: ')
        print(self.spisok)

print('Введите длину списка: ')
N = int(input())
spisok = []

n = Sort(N, spisok)
Sort.list(n)
Sort.bubble(n)
