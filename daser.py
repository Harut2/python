#=================das 18==================
# def is_prime(number):
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return 'parz chi'
#         break
#     else:
#         print('parza')
        
# def pifagor (a,b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c

# def taxi(km):
#     return 4 + (km * 1000 / 140) * 0.25

# print(taxi(2.5))

# def delivery(count):
#     return 10.95 + (count - 1) * 2.95
# print(delivery(3))

# def median(a,b,c):
#     mylist = [a,b,c]
#     mylist.sort()
#     return mylist[1]
# print(median(-6,9,3))


# def caldendar(day,month,year):
#     summ = 0
#     day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if year % 4 == 0:
#         day_list[1] - 29
#     for i in range(month - 1):
#         summ += day_list[i]
#     summ += day
#     return summ
# print(caldendar(24,10,2024))    


# def reverse_caldendar(day,year):   ===========ELSEI SXALNA============
#     summ = 0
#     day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     while True:
#        if days > day_list[0]:
#             days -=  day_list[0]
#             day_list.pop(0)
#         else:
#             break
#        return f'{days}.{month}.{year}'
# print(reverse_caldendar(2024,2997))    
#--------------------------------------------------------      kisat prata      -----------------------------------
#import random

# def random_numbers():
#     alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
#     return f'{random.randint (0, 9)}{random.randint(0, 9)}{random.}'
# print(random_numbers)



# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i * j:>4}', end = ' ')
#     print()



# def factorial(number):
#     summ = 1
#     for i in range(1,number, + 1):
#         summ *= i
#     return summ
# print(factorial(5))


# def dec_to_bin(number):
#     binary_code = ''
#     while number > 1:
#         binary_code += str (number % 2)
#         number //= 2
#         return '1' + binary_code[:: -1]
# print(dec_to_bin(120))

#---------------------------  das 19  ------------------------
# nums1 = [1,2,3,0,0,0]
# n = 3
# nums2 = [2,5,6]
# m = 3
# nums1[m:m + n] = nums2[:n]
# nums1.sort()
# print(nums1)





# nums = [3,2,2,3]
# val = 3
# while val in nums:
#    nums.remove
# print(nums)



# nums = [1,1,1,12,3,4,3,42,4,234,1]
# for i in nums.copy():
#     if nums.count(i):
#         nums.remove(i)
# print(nums)



# nums = [5,3,54,4,5,3,5,3,5,3,]
# nums.sort()
# print(nums[len(nums) // 2])


# s = "hello world"
# print(len(s.split(' ')))




# strs = ["flower", "flow","fflight"]
# strs.sort(key=len)
# index = 0
# while index < len(strs):
#     if strs[0] == strs[index][:len(strs[0])]:
#         index +=1
#     else:
#         strs[0] = strs [0][:-1]
# print(strs[0])





# def func(a,b):
#     if b == 0:
#         return a
#     else:
#         return func(b , a % b)
# print(func(1234567,98765432))


# def func(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + 1 func(mylist[2:])
#         print(func(['A ',12]))



# def func(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == list:
#         return func(mylist[0] + func(mylist[1:]))
#     else:
#         return (mylist[0] + func(mylist[1:]))
    
# print(func([1, [2, 3], [4, [5,] [6, 7]]], [[[8],9], [10]]))







# strs = ["flower", "flow","fflight"]
# strs.sort(key=len)
# index = 0
# while index < len(strs):
#     if strs[0] == strs[index][:len(strs[0])]:
#         index +=1
#     else:
#         strs[0] = strs [0][:-1]
# print(strs[0])