'''Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное
расстояние в сантиметрах, которое должна пройти черепашка.

Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу,
которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу,
которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение
начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

Программе подаётся на вход число команд n n n, которые нужно выполнить черепашке, после чего n n n строк с
самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки.
Все координаты целочисленные.

Sample Input:

4
север 10
запад 20
юг 30
восток 40

Sample Output:

20 -20'''

x = 0
y = 0
res = []

def move_tortoise(direction, distance):
    global x, y
    if direction == 'север':
        y += int(distance)
    elif direction == 'юг':
        y -= int(distance)
    elif direction == 'восток':
        x += int(distance)
    elif direction == 'запад':
        x -= int(distance)
    return [x, y]


n = int(input())

for i in range(n):
    where, dis = input().split()
    res = move_tortoise(where, dis)

print(*res)