coordinates = (35, 86, 67)

# print(coordinates[1])
x, y, z = coordinates
print(x)
print(y)
print(z)

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

num1, num2, *tmp = nums
print(num1)  # 1
print(num2)  # 2
print(tmp)  # [3, 4, 5, 6, 7, 8, 9, 10]

print(*nums, sep='⭐️', end='!\n')
# sep - separator - разделитель вывода
# end - это символ, которым заканчивается print

for num in nums:
    print(num ** 2, end='; ')
