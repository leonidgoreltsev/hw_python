
# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Задача 1
age = int (input ("введите возраст:" ))
name = (input ("введите имя:"))
print("привет", name, "которому(ой)", age)

# Задача 2
x = int (input("введите число:" ))
f = 2
print(x + f)

# Задача 3
age_for = 18
age = int (input ("введите возраст:" ))
access = 0
if age >= age_for:
    print("Доступ разрешен")
    access = 1
if age < age_for:
    print("Извините, пользование данным ресурсом только с 18 лет")
