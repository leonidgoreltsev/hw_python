# задача 1
fruits = ['apple', 'banana', 'mango']
num = 1
for fruit in fruits:
    print('{}{} {}'.format(num, '.', fruit.rjust(10, ' ')))
    num += 1

# задача 2
list2 = ['яблоко', 'банан', 'киви', 'арбуз']
list1 = ['курица', 'соль', 'лук', 'яблоко', 'банан', 'киви', 'арбуз']
set1 = set(list1)
set2 = set(list2)
list3 = list( set1.difference(set2) )
print(list3)

# задача 3. - не готова
list_num = [4, 8, 15, 16, 23, 42]
new_list = []
for num in list_num:
    if num % 2 == 0:
        new_num = num / 4
        print(new_num)

