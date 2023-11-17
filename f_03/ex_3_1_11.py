# Подвиг 11. С клавиатуры вводятся две буквы (в одну строку через пробел). Вывести на экран следующую строку:
#
# "Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"
#
# Sample Input:
#
# a z
# Sample Output:
#
# Коды: a = 97, z = 122


word_one, word_two = input().split()
print(f'Коды: {word_one} = {ord(word_one)}, {word_two} = {ord(word_two)}')
