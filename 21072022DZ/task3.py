#Создайте программу для игры в "Крестики-нолики".
print("*" * 15, " Игра Крестики-нолики для двух игроков ", "*" * 15)

desk = list(range(1,10))

def create_desk(desk):
    print('-' * 13)
    for i in range(3):
        print('|' , desk[0+i*3],'|' , desk[1+i*3],'|' , desk[2+i*3],'|')
        print('-' * 13)

def take_turn(playar_turn):
    valid = False
    while not valid:
        turn = input(f"Введите ваш ход {playar_turn} : ")
        try:
            turn = int(turn)
        except:
            print("Некорректный ввод.")
            continue
        if turn >= 1 and turn <= 9:
            if(str(desk[turn-1]) not in 'XO'):
                desk[turn-1] = playar_turn
                valid = True
            else:
                print('Тут нет места!')
        else:
            print("Некорректный ввод.")

def check_turn(desk):
    win_choise = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in win_choise:
        if desk[i[0]] == desk[i[1]] == desk[i[2]]:
            return desk[i[0]]
    return False

def action(desk):
    counter = 0
    win = False
    while not win:
        create_desk(desk)
        if counter % 2 == 0:
           take_turn("X")
        else:
           take_turn("O")
        counter += 1
        if counter > 4:
           tmp = check_turn(desk)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    create_desk(desk)

action(desk)

input("Нажмите Enter для выхода!")