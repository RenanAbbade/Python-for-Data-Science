a = 23
b = 9
m = 31
x0 = 7
xAnt = ((a * x0 + b) % m)
print("X1=",xAnt, "| R1 = ", xAnt/ m)

for i in range(2,12):
    xAnt = ((a * xAnt + b) % m)
    print("X",i,"=",xAnt, "| R",i,"= ", xAnt / m)

