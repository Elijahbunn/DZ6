number = int(input('Enter number: '))
sum = 0
dict = [(round((1 + 1/i)**i, 2)) for i in range(1, number+1)]
dict2 = []
for i in range(1, number+1):
    sum += dict[i-1]
    dict2.append(sum)
print(f'Последовательность до {number}: {dict} \nСписок сумм: {dict2}')
final_list = list(zip(dict, dict2))
print(final_list)