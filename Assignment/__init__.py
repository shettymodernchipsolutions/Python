f1 = open('sample.txt', 'r')
f2 = open('simple.txt', 'w')

Data = f1.read()
f2.write(Data)

f1.close()
f2.close()


def prime(n):
    x = True
    for i in range(2, n):
        if n % i == 0:
            x = False
            break
        else:
            x = True
    return x


a = 150
while a < 201:
    if prime(a) == True:
        print(a)
    a+=1