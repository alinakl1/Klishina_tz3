from main import maxim, summ, minim, proizv

with open("input.txt", 'r') as file:
    data = list(map(int, file.read().split()))

print("максимум:", maxim(data))
print("минимум:", minim(data))
print("сумма:", summ(data))
print("произведение:", proizv(data))