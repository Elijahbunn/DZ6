# number = str(input('Enter number: '))
# number = number.replace(',', '')
# number = number.replace('.', '')
# list = []
#sum = 0
# for i in range(len(number)):
#     list.append(int(number[i]))

# print(list)

# for i in range(len(list)):
#     sum += list[i]

# print(sum)

sum = 0
numbers1 = list(map(int, (input('Enter number: ')).replace(',', '').replace('.', ''))) #сократил количество строк кода и улучшил синтаксис при помощи функции "map"
sum_numbers = []
for i in range(len(numbers1)):
    sum += numbers1[i]
    sum_numbers.append(sum)

numbers3 = list(enumerate(zip(numbers1, sum_numbers), 1)) #улучшил вывод данных в терминале, где теперь не просто выводится конечная сумма, а пронумерованный список сумм, получившихся после добавлня каждого числа
print(*numbers3)
#print(f'{numbers1}\n {sum}')

