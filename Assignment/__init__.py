f1 = open('sample.txt', 'r')
f2 = open('simple.txt', 'w')

Data = f1.read()
f2.write(Data)

f1.close()
f2.close()


