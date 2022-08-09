# name = "Andrew" # строчный комментарий
# age = 20
# print("Hello", name, " . I am", age)

# print((type(name)))
# print((type(age)))
# print(id(age))
# a = b = c = 1
# print(a, b, c)
# a, b, c = 5, "Hello", 9.2
# import keyword
# print(keyword.kwlist)
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# a, b = b, a
# print("a:", a)
# print("b:", b)
# a = 5
# b = 7
# c = 3
# s = a + b + c
# print('сумма', s)
# print('умножение', a * b * c)
# print('среднее арифм', s/2)
# num = 10
# num += 5
# print(num)

# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print(a)
# num = num // 10
# print(num)
# b = num % 10
# print(b)
# num = num // 10
# print(num)
# c = num % 10
# print(c)
# num = num // 10
# print(num)
# d = num % 10
# print(d)
# num = num // 10
# print(num)
# res = (num % 10)*1000
# num = num // 10
# res += (num % 10)*100
# num = num //10
# res += (num % 10)*10
# num = num //10
# res += num % 10
# print(res)

# a = int(input('Введите число:'))
# print(a + 5)
# print('Первое задание')
# a = 1
# b = 2
# print('a:', a)
# print('b:', b)
# a = a + b
# b = a - b
# a = a - b
# print('a:', a)
# print('b:', b)
# print('Введите четыре числа')
# c = int(input('первое число:'))
# d = int(input('второе число:'))
# e = int(input('третье число:'))
# f = int(input('четвертое число:'))
# res = (c + d) / (e + f)
# print(round(res, 2))
# print('Второе задание')
# k = int(input('Введите  пятизначное число:'))
# a = k % 10
# num = k // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# e = num % 10
# res = a * b * c * d
# print('Произведение цифр числа', k, ':', res)
# res = (a + b + c + d)/2
# print('Среднее арифмитическое числа', k, ':', res)
# 2 ДЗ
# a = int(input('Введите  число от 1 до 99:'))
# if a == 1 or a == 21 or a == 31 or a == 41 or a == 51 or a == 61 or a == 71 or a == 81 or a == 91:
#     print(a, 'копейка')
# if 4 >= a >= 2 or 24 >= a >= 22 or 34 >= a >= 32 or 44 >= a >= 42 or 54 >= a >= 52 or 64 >= a >= 62 or \
#         74 >= a >= 72 or 84 >= a >= 82 or 94 >= a >= 92:
#     print(a, 'копейки')
# if 20 >= a >= 5 or 30 >= a >= 25 or 40 >= a >= 35 or 50 >= a >= 45 or 60 >= a >= 55 or 70 >= a >= 65 or \
#         75 >= a >= 80 or 90 >= a >= 85 or 99 >= a >= 95:
#     print(a, 'копеек')

# ДЗ 3
# print('\n КАЛЬКУЛЯТОР\nВыберете операцию:\n1 - "r" - принимает унарный минус к операнду'
#       '\n2 - "+" - сложение\n3 - "-" - вычитание \n4 - "/" - деление'
#       '\n5 - "*" - умножение\n6 - "%" - деление по модулю (остаток от деления'
#       '\n7 - "<" - минимальное из двух чисел\n8 - ">" - максимальное из двух чисел')
# try:
#     a = int(input('Введите  цифру математического знака:'))
#     b = int(input('Введите  первое число:'))
#     c = int(input('Введите  второе число:'))
#     if a == 1:
#         b = -b
#         c = -c
#         print("Результат:", b, c)
#     if a == 2:
#         print("Результат:", b + c)
#     if a == 3:
#         print("Результат:", b - c)
#     if a == 4:
#         print("Результат:", round(b / c, 2))
#     if a == 5:
#         print("Результат:", b * c)
#     if a == 6:
#         print("Результат:", b % c, "остаток от деления")
#     if a == 7:
#         print("Результат: минимальное значение", min(b, c))
#     if a == 8:
#         print("Результат: максимальное значение", max(b, c))
# except ZeroDivisionError:
#     print("Нельзя делить на 0")
# except ValueError:
#     print("Вы ввели строковое или не целое значение")

#                                     Вариант 2
# # Можете подсказать как в данной конструкции перерывать (при введенном неверном символе)  до введения чисел


# print('\n КАЛЬКУЛЯТОР\nВыберете операцию:\n1 - "r" - принимает унарный минус к операнду'
#       '\n2 - "+" - сложение\n3 - "-" - вычитание \n4 - "/" - деление'
#       '\n5 - "*" - умножение\n6 - "%" - деление по модулю (остаток от деления'
#       '\n7 - "<" - минимальное из двух чисел\n8 - ">" - максимальное из двух чисел')
# try:
#     a = str(input('Введите  математическй знак:'))
#     b = int(input('Введите  первое число:'))
#     c = int(input('Введите  второе число:'))
#     if a =='r', a =='+', a =='-', a =='/', a =='*', a =='%', a =='<', a =='>' :
#         print('Неверный математический знак')
#     if a == 'r':
#         b = -b
#         c = -c
#         print("Результат:", b, c)
#     if a == '+':
#         print("Результат:", b + c)
#     if a == '-':
#         print("Результат:", b - c)
#     if a == '/':
#         print("Результат:", round(b / c, 2))
#     if a == '*':
#         print("Результат:", b * c)
#     if a == '%':
#         print("Результат:", b % c, "остаток от деления")
#     if a == '<':
#         print("Результат: минимальное значение", min(b, c))
#     if a == '>':
#         print("Результат: максимальное значение", max(b, c))
# except ZeroDivisionError:
#     print("Нельзя делить на 0")
# except ValueError:
#     print("Вы ввели некорректное значение")


# ДЗ 4
# from random import randint
# print('Угадай число с 10 попыток')
# a = randint(1, 100)
# # print(a)
# b = int(input('Введите  Число от 1 до 100:'))
# for i in range(1, 10):
#     if b == 0:
#         print('Игра окончена')
#         print('Вы не угадали заданое число  с', i, 'раз')
#         break
#     if a > b:
#         print('Введенное число меньше  загаданного')
#         b = int(input('Введите  Число от 1 до 100:'))
#     if a == b:
#         print('Вы ввели верное число')
#         print('Вы угадали заданое число  с', i, 'раза')
#         break
#     if a < b:
#         print('Введенное число больше   загаданного')
#         b = int(input('Введите  Число от 1 до 100:'))

# ДЗ 5
# a = [input('->') for i in range(int(input('Введите элементы списка:\n n = ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end = " ")
#         i +=1
#
#
# a = [input('->') for i in range(int(input('Введите элементы списка:\n n = ')))]
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end = " ")


# # dz 6
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# k = c + b[3:5]
# print(k)
#
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in range(len(a)):
#     b = a.count(a[i])
#     if b == 1:
#         print(a[i], end=' ')
# d = []
# for i in a:
#     for j in b:
#         if i != j:
#             d.append(i)
# print(d)


# import math
# num1 = math.sqrt(16)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)
# print(dir(math))
# print(math.pi)

# rd = int(input('Введите  радиус окружности: '))
# print('Длинна окружности: ', round(2 * math.pi * rd, 2))

# import time
# seconds = time.time()
# print('Секунды с начала эпохи:', seconds)
# locale_time = time.ctime(seconds)
# print('Местное время:', locale_time)
# res = time.localtime()
# print('LocalTime:', res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
# print(time.strftime('Today is %B, %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S'))

# pause = 5
# print('Programm started...')
# time.sleep(pause)
# print(pause, 'seconds.')

# text = input('Название напоминания: ')
# local_time = float(input('Через сколько минут: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, 'секунд.')

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, 'seconds.')
# import locale
# locale.setlocale(locale.LC_ALL, '')
#
# print(time.strftime('Сегодня: %B, %d, %Y'))

# def hello(name):
#     print('Hello', name)
#
#
# hello('Irina')
# hello('Ira')

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum('abc', 'efb')
# get_sum(2.5, 4.3)


# def sympol():
#     pass
#
# sympol(9, '+', '-')
# sympol(7, 'x', '0')

# def maximum(one,two ):
#     if one > two
#         return one
#     else:
#         return two
# print(maximum(9, 16))

# x = int(input('a =  '))
# y = int(input('b =  '))
#
#
# def fun(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(fun(x, y))

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, 'v kube =', cube(i))


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b
#
# fib(15)


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
# print(is_greater(10, 5))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print("Количество символов мало")
#     else:
#         print('Недопустимые символы')
#     return False
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Это надежный пароль!')
# else:
#     print('Это ненадежный пароль!')

# def get_sum(a, b, c, d = 0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))

# def symbol(elements=20, sign = "-"):
#     for i in range(elements):
#         print(sign, end="")
#     print()
# symbol(10, "+")
# symbol(5, "*")
# symbol(7)


# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_dight = n %10
#         if event and cur_dight % 2 == 0:
#             s += cur_dight
#         elif not event and cur_dight % 2 != 0:
#             s += cur_dight
#         n //= 10
#     return s
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, event=False))
# print(digits_sum(38271, event=False))
# print(digits_sum(123456789, event=False))


# def display_info(name, age):
#     print('Name:', name, "\nAge:", age)
#
#
# display_info("Ira", 20)
# display_info(age=20, name="Igor")

# dz 7

# Список
# n = [5, 6, [7, 8, 9], "Hello", 5.6, True]
# print(n)
# print(type(n))
# print(n[0])
# print(n[2][0])
# print(n[3])
# print(n[3][1])
#
# print(n[-2])
#
# n[1] = 256
# n[3] += "100"
# n[-7] = 45
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print([5] * 6)
# print(s)
#
# b = list("Hello")
# print(b)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n is n2:
#     print('Списки равны')
# else:
#     print('Списки разные')

# [выражение for переменная in последовательность]
# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# n = 5
#
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# a = [1, 2, 3]
# b = [4]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print([int(input("-> ")) for i in range(int(input("n = ")))])

# n = [2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for elem in n:
#     print(elem, end=" ")

# n = [-3, 9, -5, -1]
# b = 0
# for i in n:
#     if i < 0:
#         b += i
#
# print(b)

# a = [int(input('Элементов списка: ')) for i in range(int(input('n = ')))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество:", k)
# print("Сумма:", s)

# a = [int(input('-> ')) for i in range(int(input('Введите кол-во элементов списка: ')))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
# print(s / k)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 9, 2, 1, 17, 25]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез
# список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])
# print(s[1:5])
# print(s[6:7])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:3] = [20]
# s[2] = 30
# s[32:] = [9, 18, 28, 38, 48]
# print(s)
#
# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец основного списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, [100, 2])  # добаляет элемент по индексу (первый параметр), с заданным значением (второй параметр)
# print(s)


# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# DZ
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
# # i = 0
#
# # while i < len(a):
# #     c.append(a[i])
# #     c.append(b[i])
# #     i += 1
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)


# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s = [5, 9, 3, 7, 1, 8]
# # s[3:] = []
# print(s)
# s.remove(9)  # удаляет первый искомый элемент из списка по значению
# print(s)
# last = s.pop(-2)  # без параметров - удаляет последний элемент из списка, указанный параметр - это индекс удаляемого
# # элемента
# print(last)
# print(s)
# s.clear()  # удаляет из списка все элементы
# print(s)
# del s[2:4]
# print(s)

# s = [int(input("-> ")) for i in range(int(input("введите ко-во элементов списка: ")))]
# # for i in range(len(s)):
# #     k = int(input('Введите индекс: '))
# #     del s[2]
# #     break
# k = int(input('Введите индекс: '))
# s.pop(k)
# print(s)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(3, 9, -1)
# print(ind)

# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# print(s)
# s.reverse()  # переворачивает список
# print(s)
# s.sort(reverse=True)  # сортирует в порядке возрастания, изменяет список, reverse=True - сортировка в порядке убывания
# print(s)
# a = sorted(s, reverse=True)  # сортирует в порядке возрастания, НЕ изменяет список
# print(a)
# print(s)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

# a = [1, 2, 3, 4, 2]
# b = [11, 12, 13]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):  # от 0 до 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # от 3 до 5
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)

# import random
#
# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
#
# print(randint(10, 15))
# print(randrange(0, 10, 2))

# DZ 6_1
# import random as r
# a = [[r.randint(-20, 10) for x in range(3)] for y in range(4)]
# b = 0
# for i in a:
#     for x in i:
#         print(x, end="\t\t")
#         if x < 0:
#             b += 1
#     print()
# print("Количество отрицательных чисел: ", b)
#
#
# a = [[r.randint(0, 4) for x in range(3)] for y in range(4)]
# b = 1
# for row in a:
#     for x in row:
#         if x > 0:
#             b *= x
#         print(x, end="\t\t")
#     print()
# print("Произведение ненулевых элементов: ", b)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 6)
# print(a)
# print(type(a))
# b = tuple((1, 2, 3, 4, 6))
# print(b)
# print(type(b))

# t = (1,)
# print(type(t))
# t1 = tuple('hello')
# print(t1)
# print(t1[1])
# print(t1[1:3])

# s1 = tuple(int(input('->')) for i in range(5))
# print(s1)

# a = tuple(2**i for i in range(1, 13))
# print(a)

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
# for i in t3:
#     print(i, end= '')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first: second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# DZ 7
# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# DZ 8
# import math
#
# print('1 - прямоугольник, 2 - треугольник, 3 - круг')
# f = input('Выберите фигуру для нахождения ее площади: ')
#
#
# def square():
#     print(' Введите длины сторон прямоугольника')
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = a *b
#     print('Плошадь прямоугольника:', round(c, 2))
# if f == '1':
#     square()
#
#
# def triangle():
#     print('Введите высоту и основания треугольника')
#     a = float(input('Высота: '))
#     b = float(input('Основание: '))
#     c = (a * b)/2
#     print('Плошадь  треугольника:', round(c, 2))
# if f == '2':
#     triangle()
#
#
# def circle():
#     print('Введите радиус круга')
#     r = float(input('Радиус круга: '))
#     print('Плошадь  круга:', (round(math.pi * (r ** 2), 2)))
# if f == '3':
#     circle()

# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# k = c + b[3:5]
# print(k)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in range(len(a)):
#     b = a.count(a[i])
#     if b == 1:
#         print(a[i], end=' ')

# DZ 9
a = ('ab', 'abcd', 'cde', 'abc', 'def')
print('Исходный кортеж:', a)
s = input(str('s='))
if s in a:
    print('Yes')
else:
    print('No')
# DZ 9.1
a = tuple(input('Введите по порядку, без пробелов, элементы кортежа:'))
oneSimbol = set(a)
# print(set(a))
print(a)
for i in oneSimbol:
    print('Количество', i, '=', a.count(i))











# a = tuple(input('Введите по порядку, без пробелов, элементы кортежа:'))
# print(a)
# arr = [i for i in a]
# c = {}
# for i in arr:
#     if i not in c:
#         c[i] = 1
#     else:
#         c[i] +=1
# print(c)

