array1 = [i for i in range(1, 100, 3)]
array2 = list(filter(lambda current: current%8==0, array1))
print(f"{array1} \n{array2}")