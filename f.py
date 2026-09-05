names = ["barbod", "shahrad", "mahbod"]
for name in names:
    print(name)

number = 1
while number <= 5:
    print(number)
    number += 1

for number in range(1, 6):
    print(number)

for number in range(1, 10):
    if number == 5:
        print(number)

for number in range(1, 6):
    if number == 3:
        print(number)

for row in range(3):
    for column in range(3):
        print(row, column)

names = ["barbod", "shahrad", "mahbod"]
for index, name in enumerate(names):
    print(index, name)

names = ["barbod", "shahrad", "mahbod"]
scores = [13, 12, 9]
for name, scores in zip(names, scores):
    print(name, scores)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 10:
        print("peyda shod")
        break
else:
    print("peyda nashod")

for number in range(5):
    if number == 2:
        pass
    print(number)