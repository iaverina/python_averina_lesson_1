# Задание 1.
#
# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
#
# Пример:
# Ведите ваше имя: Василий
# Ведите ваш пароль: vas
# Введите ваш возраст: 45
# Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45


nam = input("Input your name: ")
psw = input("Input your password: ")
age = int(input("Input your age: "))
print(f'"Your account entrance details are the following: '
      f'"your name is - {nam}, your password is - {psw}", your age is {age}"')
