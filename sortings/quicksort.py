# Реализуйте быструю сортировку.
#
# На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него. Затем рекурсивно запуститесь
# от двух частей, на которые разбился исходный массив.
#
# Формат ввода
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 10^6).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами (-10^9 ≤ ai ≤ 10^9).
#
# Формат вывода
# Выведите результат сортировки, то есть N целых чисел, разделенных пробелами.

from random import choice
n = int(input())
unsorted = list(map(int, input().split()))


def partition(predicate, lst, equal=-1, greater=-1):

    for now in range(len(lst)):
        if lst[now] == predicate:
            if equal == -1 and greater != -1:
                tmp = lst[now]
                lst[now] = lst[greater]
                lst[greater] = tmp
                equal = greater
                greater += 1
            elif equal == -1 and greater == -1:
                equal = now
            elif equal != -1 and greater != -1:
                tmp = lst[now]
                lst[now] = lst[greater]
                lst[greater] = tmp
                greater += 1
            else:
                continue
        elif lst[now] > predicate:
            if greater == -1:
                greater = now
            elif greater != -1:
                continue
        elif lst[now] < predicate:
            if equal != -1 and greater != -1:
                tmp = lst[now]
                lst[now] = lst[greater]
                lst[greater] = lst[equal]
                lst[equal] = tmp
                equal += 1
                greater += 1
            elif equal != -1:
                tmp = lst[now]
                lst[now] = lst[equal]
                lst[equal] = tmp
                equal += 1
            elif greater != -1:
                tmp = lst[now]
                lst[now] = lst[greater]
                lst[greater] = tmp
                greater += 1
            else:
                continue

    return predicate, lst, equal, greater


def quicksort(lst):

    if len(lst) <= 1:
        return lst
    else:
        x = choice(lst)

        apart = partition(x, lst)

        left = quicksort(apart[1][:apart[2]])
        right = quicksort(apart[1][apart[3]:])

        return left + apart[1][apart[2]:apart[3]] + right


result = quicksort(unsorted)

print(*result)
