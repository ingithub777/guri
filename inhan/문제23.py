f = open("E:/python/learning_python.txt",'r')
a = f.read()
f = open("E:/python/learning_python.txt",'w')
b = a.replace(("python"),("C"))
f.write(b)
# a.replace("python","C")
print(a)