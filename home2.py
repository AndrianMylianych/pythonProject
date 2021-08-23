###############################
# STRINGS
###############################

# st = 'as 23 fdfdg544'

# numbers = ""

# for i in st:
#     if i in '1234567890':
#         numbers += i

# numbers = ", " .join(numbers)

# print(numbers)

# 2

# st2 = 'as 23 fdfdg544 34'

# numb = ""

# for i in st2:
#     if i.isdigit():
#         numb += i
#     else:
#         numb += " "
# numb = ", ".join(numb.split())

# print(numb)

#############################
# list comprehension
#############################

# greeting = 'Hello, world'

# greeting = greeting.upper()

# li = []

# for i in greeting:
#     li.append(i)

# print(li)

# 2
# lis = []

# for i in range(50):
#    if i % 2 != 0:
#         lis.append(i**2)

# print(lis)

###########################
# function
###########################

# - створити функцію яка виводить ліст


#def lF(list: list):
#    print(list)


#aaa = [1, 2, 3, 4, 5, 65]

#lF(aaa)
########
#l = [1, 2, 3, 4, 5]


#def list_func(l):
#    for i in range(len(l)):
#        print(f'{i} -> {l[i]}')


#list_func(l)

#  створити функцію яка приймає три числа та
#  виводить та повертає найменьше.


#def minF(x: int, y: int, z: int):
#    if x < y and x < z:
#        print(x)
#        return x
#    elif y < x and y < z:
#        print(y)
#        return y
#    else:
#        print(z)
#        return z


#minF(34.2, 43, -110)
#######################


#def get_min(a, b, c):
#    res = min(a, b, c)
#    print(res)
#    return res


#min1 = get_min(5, 2, 3)
#print(min1)

# - створити функцію яка приймає три числа
# та виводить та повертає найбільше.


#def maxF(x: int, y: int, z: int):
#    maxN = max(x, y, z)
#    print(maxN)
#    return maxN


#maxF(45, 32, 55)

# створити функцію яка приймає будь-яку кількість чисел,
# повертає найменьше, а виводить найбільше


# def numbersF(*args):
#     minimum = min(*args)
#     print(minimum)
#     maximum = max(*args)
#     return maximum


# retur = numbersF(11, 22, 33, 44, 55, 66, 77)
# print(retur)

# створити функцію яка повертає найбільше число з ліста


# def max_listF(list: list):
#     print(max(list))


# max_listF([555, 33, 22, 665, 21, 10])

# створити функцію яка повертає найменьше число з ліста


# def min_listF(list: list):
#     print(min(list))


# min_listF([444, 33, 565, 222, 34, 222, 33.4])

# створити функцію яка приймає ліст чисел
# та складає значення елементів ліста та повертає його.


# def sumF(list: list):
#     return sum(list)


# print(sumF([33, 55, 676, 33.2, 22, 21, 221]))

# створити функцію яка приймає ліст чисел
# та повертає середнє арифметичне його значень.


# def avgF(list: list):
#     return sum(list) / len(list)


# print(avgF([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

############
# decorators
############


# def decor(f):
#     def wrap():
#         return f().replace('_', ' ')

#     return wrap


# @decor
# def pr():
#     return 'Hello_boss_!!!'


# print(pr())


# CLASSWORK

# прога, що виводить кількість кожного символа з
# введеної строки,

# st = 'as 23 fdfdg544'

# for s in set(st):
#     count = st.count(s)
#     print(f"'{s}' -> '{count}'")

# создать новый лист и записать в него 'GT' если элемент в numbers больше 4
# и 'LT' если элемент меньше или равен 4

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# new = ['GT' if x > 4 else 'LT' for x in numbers]
# print(new)

# записать в лист тюплы (x,y) если x+y == 0
# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]

# together = [(x, y) for x in list1 for y in list2 if x + y == 0]

# print(together)