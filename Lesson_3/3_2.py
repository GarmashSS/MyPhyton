# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

x= int(input("Введите число элементов : "))
# y= int(input("Введите число для сравнения : "))
list = []
while len(list) < x :
    i= int(input("Введите число : "))
    list.append(i)
print(*list)    
y= int(input("Введите число для сравнения : "))
m = abs(y - list[0])
r= list[0]
for i in range(1, len(list)):
 
    if m > abs(list[0]-y):
        m = abs(list[0]-y)
        r = list[i]
print (r)

