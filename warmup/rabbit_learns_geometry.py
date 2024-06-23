# Кролики очень любопытны. Они любят изучать геометрию, бегая по грядкам. Наш кролик как раз такой. Сегодня он решил
# изучить новую фигуру — квадрат.
#
# Кролик бегает по грядке — клеточному полю N × M клеток. В некоторых из них посеяны морковки, в некоторых нет.
#
# Помогите кролику найти сторону квадрата наибольшей площади, заполненного морковками полностью.
#
# Формат ввода
# В первой строке даны два натуральных числа N и M (, ). Далее в N строках расположено по M чисел, разделенных
# пробелами (число равно 0, если в клетке нет морковки или 1, если есть).
#
# Формат вывода
# Выведите одно число — сторону наибольшего квадрата, заполненного морковками.

n, m = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))

answer_matrix = [[0 for i in range(m)] for j in range(n)]

answer_matrix[0][0] = field[0][0]
for i in range(1, m):
    answer_matrix[0][i] = field[0][i]
for j in range(1, n):
    answer_matrix[j][0] = field[j][0]

for i in range(1, n):
    for j in range(1, m):
        if answer_matrix[i-1][j-1] != 0 and answer_matrix[i][j-1] != 0 and answer_matrix[i-1][j] != 0 and field[i][j] != 0:
            answer_matrix[i][j] = min(answer_matrix[i-1][j-1], answer_matrix[i][j-1], answer_matrix[i-1][j]) + 1
        else:
            answer_matrix[i][j] = field[i][j]

print(max(max(answer_matrix, key=lambda x: max(x))))
