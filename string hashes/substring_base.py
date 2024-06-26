# Строка S была записана много раз подряд, после чего от получившейся строки взяли префикс и дали вам. Ваша задача
# определить минимально возможную длину исходной строки S.
#
# Формат ввода
# В первой и единственной строке входного файла записана строка, которая содержит только латинские буквы, длина
# строки не превышает 50000 символов.
#
# Формат вывода
# Выведите ответ на задачу.

s = input()

n = len(s)
p = 10**9 + 7  # модуль по которому производятся рассчеты
x_ = 257  # x должен быть больше мощности алфавита строки
h = [0] * (n+1)
x = [0] * (n+1)
x[0] = 1
s = ' ' + s
for i in range(1, n+1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i-1] * x_) % p


def isequal(from1, from2, slen):
    return (
        (h[from1+slen-1] + h[from2-1] * x[slen]) % p ==
        (h[from2+slen-1] + h[from1-1] * x[slen]) % p
    )


for i in range(1, len(s)+1):
    if isequal(0+1, i+1, n-i):
        print(i)
        break
else:
    print(n)
