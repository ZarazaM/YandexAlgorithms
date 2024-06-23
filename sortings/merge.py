n = int(input())
lst_1 = list(map(int, input().split()))
m = int(input())
lst_2 = list(map(int, input().split()))


def merge(first, second):
    l, r = 0, 0
    result = []
    while l < len(first) or r < len(second):
        if l == len(first):
            result.extend(second[r:])
            break
        elif r == len(second):
            result.extend(first[l:])
            break
        elif first[l] <= second[r]:
            result.append(first[l])
            l += 1
        else:
            result.append(second[r])
            r += 1

    return result


print(*merge(lst_1, lst_2))
