def minim(num):
    minn = num[0]
    for el in num:
        if el < minn:
            minn = el
    return minn


def maxim(num):
    maxn = num[0]
    for el in num:
        if el > maxn:
            maxn = el
    return maxn


def summ(num):
    s = 0
    for el in num:
        s = s + el
    return s


def proizv(num):
    p = 1
    try:
        for el in num:
            p = p * el
    except OverflowError:
        p = "error"
    return p


data = []
with open("input.txt", 'r') as file:
    a = list(map(int, file.read().split()))

