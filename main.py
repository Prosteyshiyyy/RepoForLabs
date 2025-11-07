#1
# print("1 задание")
# temp = 15
# for i in range(10):
#     v = 1.8 * temp + 32
#     print("%.2f по фаренгейту" % v)
#     temp += 1.5

#2
# print("2 задание")
# from math import *
# g = 9.81
# l = 10
#
# for a in range(0, 61, 5):
#     v = (4 /3  * g * l * sin(a))
#     print(f"при угле: {a} скорость равна %.2f" %v)

#3
# print("3 задание")
# def mini(n):
#     k = 1
#     while True:
#         if k ** 2 > n:
#             break
#         k+=1
#     return k
# while True:
#     try:
#         n = int(input("Введите число n: "))
#         while True:
#             if n < 1:
#                 print("Введено отрицательное число")
#                 n = int(input("Введите число n: "))
#             else:
#                 break
#         break
#     except ValueError:
#         print("Введено некоректное число")
# print(mini(n))
