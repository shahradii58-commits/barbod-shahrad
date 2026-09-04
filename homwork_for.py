#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numbers:
    if number < 5:
        print(number)

#2
number = [42, 7, 91, 15, 63, 28, 4, 76, 33, 58, 12, 99, 21, 67, 38, 5, 84, 49, 73, 30]
new_list = []
for number in numbers:
    new_list.append(number * 2)
print(new_list)

#3
numbers = [42, 7, 91, 15, 63, 28, 4, 76, 33, 58, 12, 99, 21, 67, 38, 5, 84, 49, 73, 30]
total = 0
for number in numbers:
    total  += number
print(total)

#4
discounts = [10, 80, 0, 12, 8, 0, 0, 0, 12]
new_list = []

for discount in discounts:
    if discount > 0:

        new_list.append("takhfif dar")
    else:
        new_list.append("bedone takhfif")

print(new_list)