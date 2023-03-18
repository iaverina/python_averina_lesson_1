# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

n = input("Input an integer: ")
nn = n+n
nnn = n+n+n
print(int(n)+int(nn)+int(nnn))
