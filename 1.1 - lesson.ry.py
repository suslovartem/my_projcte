#Создайте два множества A и B, добавив в A 10 случайных целых чисел от 1 до 20, а в B добавив 5 случайных чисел.Вывести полученные множества на экран.
import random
A,B=set(),set()
while len(A)!=10:
    A.add(random.randint(1,20))
print(A,'длина А=',len(A))
while len(B)!=5:
    B.add(random.randint(1,20))
print(B,'длина B=',len(B))
