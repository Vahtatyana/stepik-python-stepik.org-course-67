'''Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) (-15, 12] \cup (14, 17) \cup [19, +\infty) (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).
Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы.'''

a = int(input())
if a > -15 and a <= 12:
    print('True')
elif a > 14 and a < 17:
    print('True')
elif a >= 19:
    print('True')
else:
    print('False')