import math
from array import *

koof = 0
member_C = array("f", [])
member_n = array("i", [])
member_m = array("i", [])


def member(k):
    if (k != 0):
        for i in range(k):
            print(f"C={member_C[i]} при")
            print(f"m={member_m[i]} и n={member_n[i]}\n")
    else:
        print("Вы еще не работали")


def vvod():
    while True:
        num = input(f"Введите указанное число\n")
        if num.isdigit():
            num = int(num)
            if (num == 1) or (num == 2) or (num == 3):
                return num
                break
            else:
                print("Введите Нужное число")
        else:
            print("Вы должны ввести указанное число, попробуйте снова.")


def vvod_n():
    while True:
        num = input(f"Введите переменную n\n")
        if num.isdigit():
            num = int(num)
            return num
            break
        else:
            print("Вы должны ввести положительное число, попробуйте снова.")


def vvod_m(n):
    while True:
        num = input(f"Введите переменную m\n")
        if not num.isdigit():
            print("Вы должны ввести положительное число, попробуйте снова.")
        elif n < int(num):
            print("Вы должны ввести число меньше чем n, попробуйте снова.")
        else:
            num = int(num)
            return num
            break


def reshenie(member_n, member_m, member_C):
    print("C(n-m)=n!/(m!*(n-m)!)")
    n = vvod_n()
    member_n.append(n)
    m = vvod_m(n)
    member_m.append(m)
    d = n - m
    fact(n)
    fact(m)
    fact(d)
    C = n / (m * d)
    member_C.append(C)
    print(f'C(n-m)= {C} \nпри\nn= {n}\nm= {m}\n')


def fact(count):
    math.factorial(count)


def main(koof):
    counter = 0
    print(
        "Вас приветсвует калькулятор.\nКалькулятор находится в бете, поэтому может решить только:\nC(n-m)=n!/(m!*(n-m)!)")
    while (counter < 1):
        print('нажмите 1-чтобы решить данную формулу')
        print('нажмите 2-чтобы выйти')
        print('нажмите 3-чтобы посмотреть свою историю(не сохраняется после выключения!)')
        a = vvod()
        if (a == 1):
            reshenie(member_n, member_m, member_C)
            koof = koof + 1
        elif (a == 3):
            member(koof)
        else:
            print("Работа прекращена")
            counter = counter + 1


if __name__ == '__main__':
    main(koof)
