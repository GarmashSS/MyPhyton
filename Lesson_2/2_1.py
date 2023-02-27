
n= int(input("Введите число монет"))
count1=0
count2=0
for i in range(n):
    x= int(input())
    if x==0:
        count1+=1
    else:
        count2+=1
if count1>count2:
    print(count2)
else:
    print(count1)

