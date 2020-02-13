'''Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Пример ввода: AAabBcdCC

Соответствующий вывод: A2a1b1B1c1d1C2

'''

x = input()

counter = 1
result = ''
final_code = ''

for i in range(len(x)):
    if len(x) == 1:
        final_code = x[i] + '1'
        break
    elif i == len(x) - 1:
        if x[i] == x[i - 1]:
            final_code += result
            break
        else:
            final_code += x[i] + str(counter)
            break
    elif x[i] == x[i + 1]:
        counter += 1
        result = x[i] + str(counter)
    else:
        result = x[i] + str(counter)
        final_code += result
        counter = 1

print(final_code)