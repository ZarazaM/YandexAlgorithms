# Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.
#
# Формат ввода
# В первой строке содержатся три числа: N, S и F (1 ≤ N ≤ 100, 1 ≤ S, F ≤ N), где N — количество вершин графа,
# S — начальная вершина, а F — конечная. В следующих N строках вводится по N чисел, не превосходящих 100, – матрица
# смежности графа, где -1 означает, что ребра между вершинами нет, а любое неотрицательное число — наличие ребра
# данного веса. На главной диагонали матрицы записаны нули.
#
# Формат вывода
# Последовательно выведите все вершины одного (любого) из кратчайших путей, или -1, если пути между указанными
# вершинами не существует

n, s, f = map(int, input().split())

# Матрица смежности
adjacent_matrix = []
for i in range(n):
    adjacent_matrix.append(list(map(int, input().split())))

# Посещенные вершины
visited = [False] * n

# Расстояние
dist = [-1] * n

# Кратчайшее
shortest = [-1] * n

stack = [s-1]
dist[s-1] = 0
shortest[s-1] = -1

while len(stack) > 0:
    vertex = stack.pop(0)
    visited[vertex] = True
    for neighbour in range(len(adjacent_matrix[vertex])):
        if adjacent_matrix[vertex][neighbour] == -1 or adjacent_matrix[vertex][neighbour] == 0:
            continue
        else:
            if dist[neighbour] == -1 or dist[vertex] + adjacent_matrix[vertex][neighbour] < dist[neighbour]:
                dist[neighbour] = dist[vertex] + adjacent_matrix[vertex][neighbour]
                shortest[neighbour] = vertex
                stack.append(neighbour)

path = []
cur = f-1
while cur != -1:
    path.append(cur+1)
    cur = shortest[cur]

if len(path) > 1:
    print(*path[::-1])
elif s == f:
    print(s)
else:
    print(-1)
