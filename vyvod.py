from main import maxim, summ, minim, proizv

with open("input.txt", 'r') as file:
    a = list(map(int, file.read().split()))

print("максимум:", maxim(a))
print("минимум:", minim(a))
print("сумма:", summ(a))
print("произведение:", proizv(a))