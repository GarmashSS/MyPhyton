# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

i = int(input("введите трехзначное число: "))
sum= 0 
j=0
while i != 0:
   j = i % 10
   i = i // 10
   sum += j
print(sum)