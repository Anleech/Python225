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
# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# print('Исходный кортеж:', a)
# s = input(str('s='))
# if s in a:
#     print('Yes')
# else:
#     print('No')
# # DZ 9.1
# a = tuple(input('Введите по порядку, без пробелов, элементы кортежа:'))
# oneSimbol = set(a)
# # print(set(a))
# print(a)
# for i in oneSimbol:
#     print('Количество', i, '=', a.count(i))



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




# print('Вносим изменения')
# print('Вносим измениения в клона')


# DZ 10
# k = {'a': 1, 'b': 2}
# m = {'b': 3, 'c': 4}
# l = k | m
# print(l)
 # DZ 11

# 11.1
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# x = a | b | c
# print(x)
#
# # 11.2
# a = {'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# b = {'emp3': {'name': 'Brad', 'salary': 8500}}
# c = a | b
# print(a.setdefault('emp3'))
# # print(a['emp3'])
# print(a['emp3']['salary'])
# for x in c:
#     print(x)
#     for y in c[x]:
#         print('\t', y, ":", c[x][y], sep=" ")
#
# # 11.3
# a = int(input('Введите количество студентов:'))
# b = {input('Имя студента:'): int(input('Введите балл студента:'))for i in range(a)}
# # print(b)
# c = 0
# for i in b:
#     c += b[i]
# m = round(c/a)
# print('Средний бал студентов:', m, '.','Студенты с баллом выше среднего:')
# for i in b:
#     if b[i] >= m:
#         print(i)
# DZ 12
# from math import pi
#
#
# def figure(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         return kwargs['d1'] * kwargs['d2']/2
#     if figure_type == 'square':
#         return kwargs['a']*kwargs['a']
#     if figure_type == 'trapezoid':
#         return (kwargs['a']+kwargs['b'])*kwargs['h']/2
#     if figure_type == 'circle':
#         return kwargs['r']*pi*kwargs['r']
#     else:
#         print('invalid data')
#
#
# print(figure(figure_type='rhombus', d1=10, d2=8))
# print(figure(figure_type='square', a=5))
# print(figure(figure_type='trapezoid', a=12, b=3, h=6))
# print(figure(figure_type='circle', r=18))
# print(figure(figure_type='unknown', a=1, b=2, c=3))

# DZ 13
# 13.1
# print((lambda x, y, z: x*y*z)(2, 5, 5))
# print()
# # # 13.2
# test = [{'name': 'Jennifer', 'final': 95},
#         {'name': 'David', 'final': 92},
#         {'name': 'Nikolas', 'final': 98}]
# res1 = sorted(test, key=lambda item: item['name'])
# res2 = sorted(test, key=lambda item: item['final'], reverse=True)
# print(res1)
# print(res2)
# print()
# # # 13.3
# test = [{'name': 'Jennifer', 'final': 95},
#         {'name': 'David', 'final': 92},
#         {'name': 'Nikolas', 'final': 98}]
# res_max = max(test, key=lambda item: item['final'])
# res_min = min(test, key=lambda item: item['final'])
# print(res_max)
# print(res_min)
# print()
# # 13.4
# nums = [3, 5, 7, 9, 5, 7, 2]
#
#
# def num_square(x):
#     return x**2
#
#
# def num_cobe(x):
#     return x**3
#
#
# s = list(map(num_square, nums))
# c = list(map(num_cobe, nums))
# print(s)
# print(c)

# DZ 15
# # 15.1
# s = 'I am learning Python. hello, WORLD !'
# d = s[s.index('h'):s.rindex('h')+1]
# res = s.replace(d, '')
# print(res)
# print()
# # 15.2
# s = 'I am learning Python. hello, WORLD !'
# d = s[s.index('h'):s.rindex('h')+1]
# res = s.replace(d, d[::-1])
# print(res)
# print()
# # 15.3
# s = '11 23 44 55 23 22'
# res = s.replace('23', '!!!')
# print('Ee заменяемая подстрока: 23')
# print('Новая подстрока: !!!')
# print(res)
# print()
# # 15.4
# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели."""
# E = s.count('Е')
# e = s.count(' е')
# print(s, '(', E+e, 'слов)')

# DZ 16
import csv
import math
import re
# mail_post = '12356@i.ru, 123_456@ru.name.ru, login@i.ru, логин-i@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# reg = r'\w.+'
# print(re.findall(reg, mail_post))
# print()
# DZ 17

# DZ 17
# 17.1


# def validate_name(name):
#     return re.findall(r'[\w+@-]{6,18}', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ssw0rd'))
# print()
# # 17.2
#
# test = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированны максимумы ежемесечных осадков'
# reg = r'[0-9]+[0-12]/.+[20[0-99]'
# print(re.findall(reg, test))

# DZ 18
# def NegativeNum(lst):
#     if lst == []:
#         return 0
#     else:
#         count = NegativeNum(lst[1:])
#         if lst[0] < 0:
#             count = count + 1
#         return count
#
#
# print("n =", NegativeNum([-2, 3, 8, -11, -4, 6]))
#
# def NegativeNumbers(lst):
#     if len(lst) == 1:
#         if lst[0] < 1:
#             return 1
#         else:
#             return 0
#     else:
#         if lst[0] < 1:
#             return 1 + NegativeNumbers(lst[1:])
#         else:
#             return NegativeNumbers(lst[1:])
#
#
# print("n =", NegativeNumbers([-2, 3, 8, -11, -4, 6]))

# DZ 19
# 19.1
# f = open('text.txt', 'w')
# f.write('Замена строки в текстовом документе;\nизмениения строки в списке;\nзаписать список в файл;')
# f.close()
# f1 = int(input('pos1='))
# f2 = int(input('pos2='))
# f = open('text.txt', 'r')
# read_f = f.readlines()
# print(''.join(read_f))
# f.close()
# res = read_f[f1]
# read_f[f1] = read_f[f2]+'\n'
# read_f[f2] = res + '\n'
# f = open('text.txt', 'w')
# f.writelines(read_f)
# print()
# print(''.join(read_f))
# f.close()
# # 19.2
# f = open('text.txt', 'w')
# f.write('Замена строки в текстовом документе;\nизмениения строки в списке;\nзаписать список в файл;\n')
# f.close()
# f = open('text.txt', 'r')
# read_f = f.readlines()
# read_f.reverse()
# print(''.join(read_f))
# f.close()
# f = open('text.txt', 'w')
# f.writelines(read_f)
# 19.3
# f1 = open('file1.txt', 'r', encoding='utf - 8')
# read_f1 = f1.readlines()
# f1.close()
# f2 = open('file2.txt', 'r', encoding='utf - 8')
# read_f2 = f2.readlines()
# f2.close()
# f3 = open('file3.txt', 'r', encoding='utf - 8')
# read_f3 = f3.readlines()
# f = open('file3.txt', 'w', encoding='utf - 8')
# res = read_f1 + read_f2 + read_f3
# f.writelines(res)
# print(''.join(res))
# f3.close()


# DZ 20
# class Book:
#     name_book = "name"
#     release_date = "00.00.0000"
#     publisher = "publisher"
#     genre = "genre"
#     author = "author"
#     price = "price"
#
#     def print_info(self):
#         print(f"Название книги: {self.name_book}\nГод выпуска: {self.release_date}\n"
#               f"Издатель: {self.publisher}\nЖанр: {self.genre}\n"
#               f"Автор: {self.author}\nЦена: {self.price}")
#
#     def input_info(self, name_book, release_date, publisher, genre, author, price):
#         self.name_book = name_book
#         self.release_date = release_date
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def set_name(self, name_book):  # установить имя
#         self.name_book = name_book
#
#     def get_name(self):  # получить имя
#         a = "Название книги: " + self.name_book
#         return a
#
#     def set_date(self, release_date):
#         self.release_date = release_date
#
#     def get_date(self):
#         return self.release_date
#
#     def set_publisher(self, publisher):
#         self.publisher = publisher
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_genre(self, genre):
#         self.genre = genre
#
#     def get_genre(self):
#         return self.genre
#
#     def set_author(self, author):
#         self.author = author
#
#     def get_author(self):
#         return self.author
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         a = "Цена: " + self.price
#         return a
#
# h1 = Book()
# h1.input_info("Путь шамана.Начало пути", "5.04.2018", "Эксмо", "LitRPG", "Василий Маханенко", "100р")
# h1.print_info()
# h1.set_name("Война и Мир")
# print(h1.get_name())
# h1.set_price("300р")
# print(h1.get_price())

# DZ 21
# from math import sqrt
# class Rectangle:
#     def __init__(self, l=0, w=0):
#         self.long = l
#         self.width = w
#
#     def get_long(self):
#         return self.long
#
#     def get_width(self):
#         return self.width
#
#     def set_square(self):
#         res_s = self.long * self.width
#         print('Площадь прямоугольника:', res_s)
#
#     def set_perimeter(self):
#         res_p = (self.long  + self.width)*2
#         print('Периметр прямоугольника:', res_p)
#
#     def set_hypotenuse(self):
#         res_h = sqrt(self.long**2 + self.width**2)
#         print('Гипотенуза прямоугольника:', round(res_h, 2))
#     def figura(self):
#         for i in range(self.long):
#             for i in range(self.width):
#                 print('*',end='')
#             print()
# p = Rectangle(3, 9)
# print('Длинна прямоугольника:', p.get_long())
# print('Ширина прямоугольника:', p.get_width())
# p.set_square()
# p.set_perimeter()
# p.set_hypotenuse()
# p.figura()

# DZ 22

# class Convert:
#     def __init__(self, k=0):
#         self.__k = k
#
#     @ property
#     def kg(self):
#         return self.__k
#
#     @kg.setter
#     def kg(self, k):
#         if isinstance(k, (int, float)):
#             self.__k = k
#         else:
#             print('Килограммы задаются только числами')
#
#     def pound(self):
#         return self.__k * 2.205
#
#
# c1 = Convert(12)
# print(c1.kg, 'кг => ', end='')
# print(c1.pound(), 'фунтов')
# c1.kg = 41
# print(c1.kg, 'кг => ', end='')
# print(c1.pound(), 'фунтов')

# DZ 23

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет# {self.__num} принадлежит {self.__surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def set_account(self, num, surname, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#     def get_account(self):
#         return self.__num, self.__surname, self.__percent, self.__value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_info(self):
#         print(f'Информация о счете')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def add_percent(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты успешно начислены')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у ван нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#         self.print_balance()
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner(' Дюма')
# acc.print_info()
# print()
#
# acc.add_percent()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# DZ 23
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_surname(self, surname):
#         print('-' * 20)
#         self.__surname = surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#         self.__value += self.__value * self.__percent
#         print('-' * 20)
#         print('Проценты изменены : ', end='')
#
#     def set_value(self, value):
#         self.__value = value
#         print('-' * 20)
#         print('Сумма изменена : ', end='')
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.set_num('12355')
# print(f'Измененый номер счета :#{acc.get_num()}')
# acc.set_surname('Дюма')
# print(f'Владелец изменен: {acc.get_surname()} ')
# acc.set_percent(0.04)
# print(acc.get_percent())
# acc.set_value(1101)
# print(acc.get_value())
# print()
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffi = 'EUR'
# x = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#         self.__value += self.__value * self.__percent
#         print('Проценты изменены : ', end='')
#
#     def set_value(self, value):
#         self.__value = value
#         print('Сумма изменена :', end='')
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     nm = property(get_num, set_num)
#     sn = property(get_surname, set_surname)
#     prc = property(get_percent, set_percent)
#     val = property(get_value, set_value)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.nm = "192938"
# print(f'#{acc.nm} : Измененый номер счета')
# acc.sn = 'Дюма'
# print(f'Владелец, {acc.sn} : изменен')
# acc.prc = 0.04
# print(acc.prc)
# acc.val = 1101
# print(acc.val)
#
# DZ24

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#     def is_digit(self):
#         if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
#             print("Координаты должны быть числами")
#             return False
#         return True
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print("Координаты должны быть целочисленными")
#             return False
#         return True
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#
#
# class Line(Prop):
#
#     def draw_line(self) -> None:
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#
#
# class Rect(Prop):
#
#     def draw_rect(self) -> None:
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(10.2, 20), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(7, 9), Point(12, 15))
# rect.draw_rect()
# rect.set_coords(Point(30.5, 40.2), Point(50, 60))
# rect.draw_rect()

# DZ 25

# class Liquid:
#     def __init__(self, name, density):
#         self.name = name
#         self.density = density
#
#     def edit_density(self, value):
#         self.density = value
#
#     def calc_m(self, v):
#         m = v * self.density
#         print(f'Вес {v} м^3 {self.name} составляет {m} кг.')
#
#     def calc_size(self, m):
#         v = m / self.density
#         print(f'Объем {m} кг {self.name} равен {v} м^3')
#
#     def print_info(self):
#         print(f'Жидкость "{self.name}" (плотность = {self.density} kg/m^3).')
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength
#
#     def edit_strenght(self, value):
#         self.strength = value
#
#
#
# l = Alcohol('Wine', 1064.2, 14)
# l.print_info()
# l.edit_density(1000)
# l.print_info()
# print()
# l.calc_m(0.5)
# l.calc_size(300)
# print()
# print(l.strength)
# l.edit_strenght(20)
# print(l.strength)

# DZ 26
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = '17'
#             self.ram = 16
#
#         def show(self):
#             print(f' => {self.brand}, {self.cpu}, {self.ram}')
#
# s1 = Student('Roman')
# s2 = Student('Vladimir')
# s1.show()
# s2.show()

# DZ 27.1
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.__DAY
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError()
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def get_format_time(self):
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом ")
#         s = self.sec % 60  # секунды
#         m = (self.sec // 60) % 60  # минуты
#         h = (self.sec // 3600) % 24  # часы
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 12
# c1["min"] = 20
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())
# print()
# # DZ 27.2
# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый операнд должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}, {self.__z}"
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     @staticmethod
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("Ни одна из координат второго операнда не должна быть равна 0")
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print("Неверно задан ключ")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             elif key == 'y':
#                 self.__y = value
#             elif key == 'z':
#                 self.__z = value
#         else:
#             print("Координаты должны быть числами")
#
#
# pt1 = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки: ", pt1)
# print("Координаты 2-й точки: ", pt2)
#
# pt3 = pt1 + pt2
# print(f"Сложение координат: ({pt3})")
#
# pt4 = pt1 - pt2
# print(f"Разность координат: ({pt4})")
#
# pt5 = pt1 * pt2
# print(f"Произведение координат: ({pt5})")
#
# pt6 = pt1 / pt2
# print(f"Частное координат: ({pt6})")
#
# print(f"Равенство координат: {pt1 == pt2}")
#
# print("x =", pt1['x'], "x1 =", pt2['x'])
# print("y =", pt1['y'], "y1 =", pt2['y'])
# print("z =", pt1['z'], "z1 =", pt2['z'])
#
# pt1['x'] = 20
# print("Запись значения в координату x:", pt1['x'])


# DZ 26
# import math
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#     def draw(self):
#         pass
#
#     def print_info(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, a, color):
#         self.a = a
#         super().__init__(color)
#
#     def square(self):
#         return self.a * self.a
#
#     def perimeter(self):
#         return 4 * self.a
#
#     def draw(self):
#         for i in range(self.a):
#             for j in range(self.a):
#                 print('*', end='')
#             print()
#
#     def print_info(self):
#         print(f'===Квадрат===\nСторона: {self.a}\nЦвет: {self.color} \nПлощадь: {self.square()} '
#               f'\nПериметр: {self.perimeter()}')
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b, color):
#         self.a = a
#         self.b = b
#         super().__init__(color)
#
#     def square(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return (self.a + self.b) * 2
#
#     def draw(self):
#         for i in range(self.a):
#             for j in range(self.b):
#                 print('*', end='')
#             print()
#
#     def print_info(self):
#         print(f'===Прямоугольник===\nДлинна: {self.a}\nШирина: {self.b}\nЦвет: {self.color} \nПлощадь: {self.square()} '
#               f'\nПериметр: {self.perimeter()}')
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c, color):
#         self.a = a
#         self.b = b
#         self.c = c
#         super().__init__(color)
#
#     def square(self):
#         p = (self.a + self.b + self.c) / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
#     def perimeter(self):
#         return (self.a + self.b + self.c) / 2
#
#     def draw(self):
#         rows = []
#         for i in range(self.c):
#             rows.append(' ' * i + '*' * (self.a - 2 * i) + ' ' * i)
#         print('\n'.join(reversed(rows)))
#
#     def print_info(self):
#         print(f'===Треугольник===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\nЦвет: {self.color} \n'
#               f'Площадь: {self.square():.2f}\nПериметр: {self.perimeter()}')
#
#
# s = Square(3, 'red')
# r = Rectangle(3, 7, 'green')
# t = Triangle(11, 6, 6, 'yellow')
# s.print_info()
# s.draw()
# print()
# r.print_info()
# r.draw()
# print()
# t.print_info()
# t.draw()

# DZ 27

# class OldOrder:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value <= 0:
#             raise ValueError(f'{self.__name} число должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = OldOrder()
#     amount = OldOrder()
#
#     def __init__(self, name, price, amount):
#         self.name = name
#         self.price = price
#         self.amount = amount
#
#     def sum(self):
#         return self.price * self.amount
#
#
# o = Order('apple', 5, 10)
# print(o.sum())

# # DZ 28
# class Integer:
#     @classmethod
#     def verify(cls, coord):
#         if not isinstance(coord, int) or coord <= 0:
#             raise TypeError(f"Координата {coord} должна быть положительным целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify(value)
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     __a = Integer()
#     b = Integer()
#     c = Integer()
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.b = b
#         self.c = c
#
#     def existence(self):
#         if (self.__a + self.b > self.c) and (self.__a + self.c > self.b) and (self.b + self.c > self.__a):
#             return "существует"
#         else:
#             return "не существует"
#
#     def info(self):
#         print(f"Треугольник со сторонами ({self.__a}, {self.b}, {self.c}) {self.existence()}")
#
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
#
# t1.info()
# t2.info()
# t3.info()

# # DZ 30.10
# from Employee import *
#
# print('Расчет заработной платы')
# print('='*50)
# a = admin.Admin(1, 'Валерий Задорожный')
# a.show_info()
# print()
# w = worker.Worker(2, 'Илья Кромин', 6)
# w.show_info()
# print()
# m = manager.Manager(3, 'Николай Хорольский', 25)
# m.show_info()
#  DZ 30

# import json
#
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])

# DZ 31
# import json
#
# data = {"Россия": "Москва"}
#
#
# def load_data(func):
#     def wrap(*args, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         func(*args, filename)
#         print("Файл сохранен")
#     return wrap
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     @load_data
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     @load_data
#     def delete_country(cls, del_country, filename):
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     @load_data
#     def search_data(cls, country, filename):
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     @load_data
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break
# DZ 33

# import csv
# #
# # with open('data2.csv', 'r') as f:
# #     reader = csv.reader(f, delimiter=';')
# #     for row in reader:
# #         print(row)

# DZ 34
# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("iternet-shop.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\n", delimiter=";")
#         writer.writerow((data['kod'], data['name'], data['price']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     mains = soup.find('div', class_='goods_container')
#     blocks = mains.find_all('div', class_='good_block')
#
#
#     for block in blocks:
#         kod = block.find('div', class_='id').find('span').find('span').text
#         name = block.find('span', class_='title').text
#         price = block.find('div', class_='price3').text
#         data = {'kod': kod, 'name': name, 'price': price}
#         print(data)
#         write_csv(data)
#
#
# def main():
#     url = 'https://satro-paladin.com/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# DZ35
# import json
#
# data = {"Россия": "Москва"}
#
#
# def load_data(func):
#     def wrap(*args, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = {}
#         func(*args, filename)
#         print("Файл сохранен")
#     return wrap
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f'{self.country}: {self.capital}'
#
#     @classmethod
#     @load_data
#     def add_country(cls, new_country, new_capital, filename):
#
#         data[new_country] = new_capital
#
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @classmethod
#     @load_data
#     def delete_country(cls, del_country, filename):
#         if del_country in data:
#             del data[del_country]
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     @load_data
#     def search_data(cls, country, filename):
#         if country in data:
#             print(f"Страна {country} столица {data[country]} есть в словаре!")
#         else:
#             print(f"Страна {country} отсутствует в словаре")
#
#     @classmethod
#     @load_data
#     def change_capital(cls, country, new_value, filename):
#
#         if country in data:
#             data[country] = new_value
#
#             with open(filename, "w") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# index = ''
# filename1 = 'list_capital.json'
# with open(filename1, "w") as fw:
#     json.dump(data, fw, indent=2, ensure_ascii=False)
#
# while index != 6:
#     try:
#         print("*" * 40)
#         index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n'
#                           '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
#                           '6 - завершение работы\nВвод: '))
#         if index == 1:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             capital_name = input("Введите название столицы страны (с заглавной буквы): ")
#             CountryCapital.add_country(country_name, capital_name, filename='list_capital.json')
#         if index == 2:
#             country_name = input("Введите страну для удаления (с заглавной буквы): ")
#             CountryCapital.delete_country(country_name, filename='list_capital.json')
#         if index == 3:
#             country_name = input("Введите название страны (с заглавной буквы): ")
#             CountryCapital.search_data(country_name, filename='list_capital.json')
#         if index == 4:
#             country_name = input("Введите название страны столицу которой хотите изменить (с заглавной буквы): ")
#             new_capital = input("Введите новое название столицы: ")
#             CountryCapital.change_capital(country_name, new_capital, filename='list_capital.json')
#         if index == 5:
#             CountryCapital.load_from_file(filename='list_capital.json')
#     except IndexError:
#         break

# DZ 36


# from bs4 import BeautifulSoup
# import requests
# from parse import Parser
#
#
# def main():
#     pars = Parser('https://satro-paladin.com/', 'internet_magazin.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method !="GET":
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return 'HTTP/1/1 200 OK\n\n', 200
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Page Not Found!</h3>'
#     elif code == 405:
#         return '<h1>404</h1><h3>Method Not Allowed!</h3>'
#     return URLS[url]()
#
#
# def generate_responce(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         responce = generate_responce(request.decode())
#         client_socket.sendall(responce)
#         client_socket.close()
#
#
# if __name__ =='__main__':
#     run()

# import sqlite3 as sq
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # summa REAL,
    # data TEXT
    # )""")

import sqlite3 as sq

with sq.connect("users.db") as con:
    cur = con.cursor()
    cur.execute("""

    CREATE  TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone BLOB NOT NULL DEFAULT '+79090000000',
    age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    email TEXT UNIQUE
    )
    """)
    cur.execute("""
        INSERT INTO person(email, ame, age) 
        VALUES (1, 'Ирина', '+79999999999', 23, 'irina@mail.ru')
         """)





    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)
    # cur.execute("""
    #     ALTER TABLE person_table
    #     ADD COLUMN addres TEXT
    #     """)
    # cur.execute("""
    #     ALTER TABLE person_table
    #     RENAME COLUMN addres TO home_address;
    # """)










