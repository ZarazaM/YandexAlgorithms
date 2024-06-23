# Реализуйте сортировку слиянием.
#
# На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с помощью уже реализованной функции.
#
# Формат ввода
# В первой строке входного файла содержится число N — количество элементов массива (0 ≤ N ≤ 10^6).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами (-10^9 ≤ ai ≤ 10^9).
#
# Формат вывода
# Выведите результат сортировки, то есть N целых чисел, разделенных пробелами, в порядке неубывания.

def merge(first, second):
    left, right = 0, 0
    result = []
    while left < len(first) or right < len(second):
        if left == len(first):
            result.extend(second[right:])
            break
        elif right == len(second):
            result.extend(first[left:])
            break
        elif first[left] <= second[right]:
            result.append(first[left])
            left += 1
        else:
            result.append(second[right])
            right += 1

    return result


n = int(input())
unsorted = list(map(int, input().split()))


def mergesort(lst):
    if len(lst) <= 1:
        return lst
    else:
        ind = len(lst) // 2
        left = mergesort(lst[:ind])
        right = mergesort(lst[ind:])
        return merge(left, right)


print(*mergesort(unsorted))
