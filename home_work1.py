""""
Задача 10: На столе лежат n монеток. Некоторые из
них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
 монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
   одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
n = int(input())
k = 0
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
if k<n/2:
    print( k)

else:
    print(n - k)

""""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел 
S и их произведение P. Помогите Кате отгадать задуманные Петей числа
"""

from math import sqrt
s, p = map( int, input('s, p = ').split() )
z = sqrt( (s/2)**2 - p )
print( int( s/2 - z ), int( s/2 + z ) )

"""""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

"""""

p = int(input("Показатель степени: "))
n = int(input("Предел: "))
 
i = 1
while i ** p <= n:
    print(i ** p, end=' ')
    i += 1
 
print("\nПоследнее число,"
      " возведенное в степень:", i - 1)
