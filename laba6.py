def LegitCheck():
    while True:
        try:
            m = int(input("Введите кол-во элементов в списке: "))
            if m > 0:
                break
            else:
                print("Введено некоректное число")
                continue
        except ValueError:
            print("Что-то не то вы ввели!")
    return m
##############1 задание ###########
print("1 zadanie")
s = input("Введите строку S: ")
s0 = input("Введите строку S0: ")
print(s0 in s)
#############2 Задание####################
print("Zadanie 2")
sogllowcaseEng = 'qwrtpsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
sogllowcaseRus= "йцукнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ"
while True:
    try:
        n = int(input("Сколько слов будет? "))
        if n > 0:
            break
        else:
            print("Такого не может быть!")
            continue
    except ValueError:
        print("Вы ввели что-то не то :(")
def craeateslice(n):
    words = []
    for i in range(n):
        words.append(input("Введите слово: "))
    return words
def countglas(word):
    counter = 0
    for i in range(len(word)):
        if word[i] in sogllowcaseEng or word[i] in sogllowcaseRus:
            counter += 1
    return counter/len(word)
words = craeateslice(n)
answer = ''
maxCap = -100
for i in range(len(words)):
    if countglas(words[i]) > maxCap:
        answer = words[i]
        maxCap = countglas(words[i])
print(f"в слове '{answer}' самая большая доля согласных")
#############3 Задание####################
print("Zadanie 3")
from random import randint
def createrandomslice(number):
    numbres = []
    for i in range(number):
        numbres.append(randint(0, 10))
    return numbres
num = LegitCheck()
numbers = createrandomslice(num)
pointer1 = 0
pointer2 = 0
countZero = 0
for i in range(len(numbers)):
    if numbers[i] == 0:
        countZero += 1
print(f"получившийся список: {numbers}")
if countZero >= 2:
    for i in range(len(numbers)):
        if numbers[i] == 0:
            pointer1 = i
            break
        else:
            continue
    for i in range(pointer1+1, len(numbers)):
        if numbers[i] == 0:
            pointer2 = i
            break
    endList = numbers[pointer1 + 1:pointer2]
    summa = 0
    for i in range(len(endList)):
        summa += endList[i]
    print(f"список элементов между нулевыми элементами: {endList}")
    print(f"сумма элементов между 1м и 2м нулевыми элементами равна = {summa}")
if countZero <2:
    print("в полученном списке меньше 2х нулевых элементов ")


temp = 0
for i in range(0,len(numbers)-1, 2):
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
print(numbers)





