x = [1, 2, 3, 4, 4, '5',"educative"]
y = [4,"educative", 4, '5', 6, 7, 8,"edu"]

a = list(set(x) & set(y))
print(a)