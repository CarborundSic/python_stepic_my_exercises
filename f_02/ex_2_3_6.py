# Подвиг 6. Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе),
# используя формулу. Выведите результат в консоль в виде целого числа с помощью функции print.
#
# Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
#
# Sample Input:
#
# 6 3
# Sample Output:
#
# 20


import math
# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print(math.trunc(c))
