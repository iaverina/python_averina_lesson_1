# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
#
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600

time_sec = int(input("Input time in seconds: "))
time_min = float(time_sec / 60)
time_hrs = float(time_sec / 3600)
print(f"{time_hrs}: {time_min}: {time_sec}")

