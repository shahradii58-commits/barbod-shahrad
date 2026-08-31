lst1 = [100, 200, 300]
lst1.insert(3, 'barbod')
print(lst1)
lst1.append('world')
print(lst1)

lst2 = [400, 500, 600]
lst1.extend(lst2)
print(lst1)

lst1.remove(100)
print(lst1)

lst1.pop(2)
print(lst1)

lst1.clear()
print(lst1)

lst3 = [a, g, b, d]
lst3.sort()
print(lst3)