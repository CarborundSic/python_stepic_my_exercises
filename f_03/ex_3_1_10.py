# Подвиг 10. Написать программу ввода двух слов (через пробел в одну строчку). Определить булевы значения для оператора
# in проверки вхождения первого слова во второе. А также для операторов ==, >, <. Все булевы значения объединить в одну
# строку через пробел и вывести на экран.
#
# Sample Input:
#
# hello python
# Sample Output:
#
# False False False True


word_one, word_two = input().split()
print(word_one in word_two, word_one == word_two, word_one > word_two, word_one < word_two)
