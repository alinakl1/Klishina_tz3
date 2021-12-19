def minim(ar):
    minn = ar[0]
    for el in ar:
        if el < minn:
            minn = el
    return minn


def maxim(ar):
    maxn = ar[0]
    for el in ar:
        if el > maxn:
            maxn = el
    return maxn


def summ(ar):
    s = 0
    for el in ar:
        s = s + el
    return s


def proizv(ar):
    p = 1
    try:
        for el in ar:
            p = p * el
    except OverflowError:
        p = "error"
    return p


with open("input.txt", 'r') as file:
    a = list(map(int, file.read().split()))
