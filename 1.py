# Условия задач
# 2. Сформируйте из введённого числа обратное по порядку входящих в него цифр и выведите на экран.
# Например: введено число 3486, то нужно вывести число 6843
# 1. Есть пятизначное натуральное число. Найдите его наибольшую цифру.
# Например: введено число 76458, наибольшая цифра в нём 8.
try:
    print("Задание 2: отобразить в обратном порядке введенное число")
    a2 = input("Введите число:\n")
    print(a2[::-1])
    print("Задание 1: Найдем наибольшую цифру введенного числа")
    a1 = input("Введите 5-значное число:\n")
    if 9999 < int(a1) < 100000: # Создаем условие чтобы число было обязательно 5значным
          pass
    else:
        print("число не 5-значное")
    q1 = int(a1[0]); q2 = int(a1[1]); q3 = int(a1[2]); q4 = int(a1[3]); q5 = int(a1[4])
    if q1>q2 and q1>q3 and q1>q4 and q1>q5: print("Введенное число", a1[0], "- наибольшее")
    if q2>q1 and q2>q3 and q2>q4 and q2>q5: print("Введенное число", a1[1], "- наибольшее")
    if q3>q1 and q3>q2 and q3>q4 and q3>q5: print("Введенное число", a1[2], "- наибольшее")
    if q4>q1 and q4>q2 and q4>q3 and q4>q5: print("Введенное число", a1[3], "- наибольшее")
    if q5>q1 and q5>q2 and q5>q3 and q4<q5: print("Введенное число", a1[4], "- наибольшее")
    if q1==q2 and q1==q3 and q1==q4 and q1==q5: print("Все введенные числа равны")
except ValueError: print("вы ввели не число а строку")