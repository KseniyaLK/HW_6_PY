#Создайте программу для игры в "Крестики-нолики".


from hashlib import new




new_list = list(range(1,10))

def func_draw (new_list): #вывод поля игры
    for i in range (3):
        print('|', new_list[0+i*3], '|', new_list[1+i*3], '|', new_list[2+i*3], '|')
    return new_list
 


def func_input(nums):#ввод позиции игроков и проверка собранной информации
    a = False
    while not a:
        num_input = input("номер позиции " + nums+ "? ")
        try:
            num_input = int(num_input)
        except:
            print ("Некорректный ввод. Введите число.")
            continue
        if  num_input >= 1 and num_input <= 9:
            if (str(new_list[num_input-1]) not in "xo"):
                new_list[num_input-1] = nums
                a = True
            else:
                print ("Эта клетка занята. Попробуйте другую.")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9.")


def func_winning(new_list): # прописываем выигрышные варианты
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win:
        if new_list[i[0]] == new_list[i[1]] == new_list[i[2]]:
            return new_list[i[0]]
    return False  

    


def func_game(new_list):# основня функция
    count = 0 #вводим счетчик ходов 
    b = False
    while not b:
        func_draw(new_list)
        if count % 2 == 0: 
            func_input("x")
        else:
            func_input("o")
        count += 1
        if count > 4:
            temp = func_winning(new_list)
            if temp:                
                print (temp, "выиграл! Мои поздравления!")
                b = True
                break
        if count == 9:
            print ("Ура! Победила дружба!")
            break
    func_draw (new_list)    
  
func_game(new_list)  






