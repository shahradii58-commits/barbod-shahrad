number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
var_a = []
for var_a in number:
    if var_a < 5:
        print(var_a)
"2:"
number_2 = [42,7,91,15,63,28,4,76,33,58,12,99,21,67,38,5,84,49,73,30]
empty_l = []
for numbers in number_2:
    empty_l.append(numbers * 2)
print(empty_l)
"3:"
list_1 = [42, 7, 91, 15, 63, 28, 4, 76, 33, 58, 12, 99, 21, 67, 38, 5, 84, 49, 73, 30]
print(sum(list_1))
"4:"
list_2 = [10,80,0,12,8,0,0,0,12]
empty_2 = []

for a in list_2:
    if a > 0:
        empty_2.append("تخفیف دار")
    else:
        empty_2.append("بدون تخفیف")
print(empty_2)