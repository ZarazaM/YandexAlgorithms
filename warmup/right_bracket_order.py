# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа должна определить,
# является ли данная скобочная последовательность правильной. Пустая последовательность является правильной. Если
# A — правильная, то последовательности (A), [A], {A} — правильные. Если A и B — правильные последовательности, то
# последовательность AB — правильная.
#
# Формат ввода
# В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.
#
# Формат вывода
# Если данная последовательность правильная, то программа должна вывести строку "yes", иначе строку "no".

order = input()
stack = []

flag = False
for i in order:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
    elif i == ')' and stack and stack[-1] == '(':
        stack.pop()
    elif i == '}' and stack and stack[-1] == '{':
        stack.pop()
    elif i == ']' and stack and stack[-1] == '[':
        stack.pop()
    else:
        flag = True
        break

if stack or flag:
    print('no')
else:
    print('yes')
