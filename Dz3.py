# Задача 1: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5 - размер массива
# 1,2,3,4,5 - данные массива
# 3 - сколько раз встречаеться число
# -> 1 - ответ

# a=int(input("Enter The Size Of The Array>")) # пользователь вводит размер массива
# b = list() # создание пустого списка
# c=int(input("Enter the number that you want to know how many times it is found in the list>")) # Число которое нужно посчитать
# for i in range(a): # цикл выполнится a раз
#     n = int(input("Enter a natural number that you want to add>")) # пользователь вводит целое число
#     b.append(n) # сохранение элемента в конец списка
# print(b.count(c)) # Считает число с в списке b

# Задача 2: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

# n=int(input("Enter The Size Of The Array>"))
# a=[int(input("Enter the number>")) for i in range(n)]
# c=int(input("Enter the number that you want to know how many times it is found in the list>")) 
# b=[abs(a[i]-c) for i in range(len(a))]
# print(a[b.index(min(b))]) 

# *Задача 3: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# dict = 'qwertyuiopasdfghjklzxcvbnm'
# list_1 = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# word = input("Enter the word>")
# if word[0].lower() in dict:
#     sum = 0
#     for letter in word:
#         for key, value in list_1.items():
#             if letter.upper() in value:
#                 sum += key
#     print(f'The number of points for this word = {sum}')