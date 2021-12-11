# print("Secure connection has been established to the bank server")
#
# try:
#     p = int(input('Enter the principal amount: \n'))
#     t = int(input('Enter the duration: \n'))
#     r = 10
#     si = (p*t*r) / 100
#     print('Simple Interest: ', si)
# except:
#     print('Enter the numerical value')
# print('Secure connection has been closed by the bank server')


# print("Secure connection has been established to the bank server")
#
# try:
#     p = int(input('Enter the principal amount: \n'))
#     t = int(input('Enter the duration: \n'))
#     r = 10
#
# except:
#     print('Enter the numerical value')
#
# else:
#     si = (p * t * r) / 100
#     print('Simple Interest: ', si)
#
# print('Secure connection has been closed by the bank server')


# print('Execution started normally')
# lst = [10, 20, 0, 40, 50]
# d = {1:'c', 2:'java', 3:'python', 4:'c++'}
#
# try:
#     r = int(input('Enter the key: '))
#     print(d[r])
#     m = int(input('Enter the numerator: '))
#     n = int(input('Enter the denominator: '))
#     print(lst[m] / lst[n])
# except KeyError:
#     print('Invalid key value')
# except IndexError:
#     print('Index out of bound')
# except ZeroDivisionError:
#     print('Division by zero')
# except:
#     print('Hey some issue occured')
#
# print('Execution terminated normally')


# print('Execution started normally')
# lst = [10, 20, 0, 30, 40]
# d = {1:'c', 2:'java', 3:'python', 4:'c++'}
#
# try:
#     r = int(input('Enter the rank: '))
#     print(d[r])
#     num = int(input('Enter the numerator: '))
#     den = int(input("Enter the denominator"))
#     print(lst[num] / lst[den])
# except KeyError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except ZeroDivisionError as  e:
#     print(e)
# except Exception as e:
#     print(e)
#
# print('Execution terminated normally')

# def fun2():
#     print('fun2() started execution')
#     num = int(input('Enter the numerator: '))
#     den = int(input('Enter the denominator: '))
#     res = num / den
#     print('Result: ', res)
#     print('fun2() finished execution normally')
#
#
# def fun1():
#     print('fun1() started execution')
#     fun2()
#     print('fun2() finished execution normally')
#
#
# def main():
#     print('main() started execution')
#     fun1()
#     print('main() finished execution normally')
#
#
# main()


def fun2():
    print('fun2() started execution')
    num = int(input('Enter the numerator: '))
    den = int(input('Enter the denominator: '))
    res = num / den
    print('Result: ', res)
    print('fun2() finished execution normally')


def fun1():
    print('fun1() started execution')

    try:
        fun2()
    except ZeroDivisionError:
        print('Exception handled in fun1()')

    print('fun2() finished execution normally')


def main():
    print('main() started execution')
    fun1()
    print('main() finished execution normally')


main()
