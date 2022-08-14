# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.
# *Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

import re

ex = '12*2-2*5-10/10'

# res = eval(ex) #ВСТРОЕННЫЙ МЕТОД
# print(res)



new_ex = re.findall(r"\d+|\D", ex)
print(new_ex)


def res(new_ex): #РАБОТАЕТ БЕЗ УЧЕТА ПРИОРИТЕТА ОПЕРАЦИЙ!! НУЖНО ДОДЕЛЫВАТЬ!!
    res = int(new_ex[0])
    for i in range(1, len(new_ex)):
        if (new_ex[i] != '+') and (new_ex[i] != '-') and (new_ex[i] != '*') and  (new_ex[i] != '/'):
            i += 1
        elif new_ex[i] == '/':
            #a = int(new_ex[i-1]) / int(new_ex[i+1])
            res /= int(new_ex[i+1])
        elif new_ex[i] == '*':
            #a = int(new_ex[i-1]) * int(new_ex[i+1])
            res *= int(new_ex[i+1])
        elif new_ex[i] == '+':
            res += int(new_ex[i+1])
        elif new_ex[i] == '-':
            res -= int(new_ex[i+1])
        
    return res       

result = res(new_ex)
print(result)



