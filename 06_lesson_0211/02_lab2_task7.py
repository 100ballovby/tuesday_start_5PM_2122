nums = [10, 5, 3, 0, 7, 8, 0, 6, 2]
middle = sum(nums) / len(nums)

for i in range(len(nums)):  # повторить <длина списка> раз
    if nums[i] == 0:
        nums[i] = middle

print(nums)


