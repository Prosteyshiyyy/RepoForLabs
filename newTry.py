from random import *
# 1 task
#если сумма индексов больше чем веденный нами размер матрицы то элемент находится ниже побочной диагонали
def legitCheck():
    while True:
        try:
            n = int(input("Введите число: "))
            if n > 0:
                break
            else:
                print("Ошибка, введите значение")
                continue
        except ValueError:
            print("Ошибка, введите значение")
    return n


def creatematr(n:int):
    matr = [[randint(1,100) for _ in range(n)] for _ in range(n)]
    return matr
def coolprint(matr:list):
    for i in matr:
        print(i)

def minMatr(matr: list, n: int):
    minimum = +float('inf')
    for i in range(len(matr)):
        for j in range(len(matr)):
            if i + j > (n-1):
                if matr[i][j] < minimum:
                    minimum = matr[i][j]
    return minimum

n = legitCheck()
matr1 = creatematr(n)
coolprint(matr1)
print(minMatr(matr1,n))

#2 task
def IsLeapYear(y:int):
    if (y % 4 == 0) and not(y % 100 == 0 and y % 400 != 0):
        return True
    else:
        return False

print(IsLeapYear(2012))

# 3 task
def ShowDem():
    n = legitCheck()
    d = {}
    for i in range(n):
        text = input('Введите страну: ')
        d[text] = (input("Введите реку: "))
    l = input("Введите реки через пробел").split()
    for key,value in d.items():
        for i in range(len(l)):
            if value == l[i]:
                print(f"Река: {l[i]} страна: {key}")
#answer
ShowDem()



















