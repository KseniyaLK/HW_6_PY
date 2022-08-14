# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



with open('folder/file28.txt', 'r') as data:
    text = data.read()

print(f'исходный текст {text}')    


def func_cod(txt):
    count = 1
    result = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[-2] != txt[-1]):
        result = result + str(count) + txt[-1]
    return result

print(f"Текст на выходе: {func_cod(text)}")

f = open('folder/file28_1.txt', 'w')
f.writelines(func_cod(text))
f.close
