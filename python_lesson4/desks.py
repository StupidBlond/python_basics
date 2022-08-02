# 3 classes, x = number of pupils in each class,
x1 = int(input("class1:"))
x2 = int(input("class2:"))
x3 = int(input("class3:"))
y1 = x1 // 2
y2 = x2 // 2
y3 = x3 // 2
z1 = x1 % 2
z2 = x2 % 2
z3 = x3 % 2
print("desks:", (y1 + z1) + (y2 + z2) + (y3 + z3))

