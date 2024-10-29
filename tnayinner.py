#------------------------------------------------------ 1 in xndir))) 
# def func(exo):
#     for i in range(2, (int(exo ** 0.5) + 1)):
#         if exo % i == 0:
#             return('parz chi')
#     else:
#         return ('parza')
# print(func(int(input('enter the number'))))    
#------------------------------------------------------2 xndir
# def pifagor(a,b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return(c)
# print(pifagor(3,4))
#------------------------------------------------------3 xxndir
# def taxi(km):
#     return f'$ {round(4 + (km * 1000 / 140 ) * 0.25)}'

# print(taxi(2))

#------------------------------------------------------4 xndir
# def x(count):
#     return 10.95 + (count - 1) * 9.25

# print(x(6))
#------------------------------------------------------5 xndir
# def median(a,b,c):
#     mylist = [a,b,c]
#     mylist.sort()
#     return mylist[1]
# print(median(1,-1,2))
#------------------------------------------------------6 xndir
# def number_to_text(number):
#     text_ = {
#         1:'One',
#         2:'Two',
#         3:'Three',
#         4:'Four',
#         5:'Five',
#         6:'Six',
#         7:'Seven',
#         8:'Eight',
#         9:'Nine',
#         10:'Ten',
#         11:'Eleven',
#         12:'Twelve'
#     }
#     return text_[number]
# print(number_to_text(11))
#------------------------------------------------------7 xndir
# def calendar(day,month,year):
#     summ = 0
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#         for i in range(month - 1):
#             summ += day_list[i]
#         summ += day
#         return(summ)
# print(calendar(23,10,2024))
#----------------------------------------------------8 xndir
# import random

# def random_numbers():
#     alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     return f'{random.randint(0, 9)}{random.randint(0, 9)} {random.choice(alphabet)}{random.choice(alphabet)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
# print(random_numbers())
#----------------------------------------------------9 xndir
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i * j :>4}', end = ' ')
#     print()
#-----------------------------------------------------10 xndir
# def factorial(number):
#     summ = 1
#     for i in range(1, number + 1):
#         summ *= i
#     return summ
# print(factorial(5))

173,174,176,181,186,meke dajanutyun((((