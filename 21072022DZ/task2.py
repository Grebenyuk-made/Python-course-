#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. 
#Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

import random 

def player_move(number_pl:int, numbers_candies:int, game_mode:int)-> int:
    match game_mode:
        case 1:
            while True:
                try:
                    move = int(input(f'Игрок {number_pl}, введи сколько конфет возьмёшь помни больше 28 нельзя брать: '))
                    if( 1<= move <= 28 ) and (move <= numbers_candies):
                        return move
                    else:
                        print('ERRO(Можно взять конфет в диапозоне от 1 до 28)')
                except:
                    print('\nERROR(Ввели некорректные данные)')
        case 2: 
            if numbers_candies >= 28:
                move = random.randint(1,28)
                print(f'\nБот забирает {move} конфет!')
                return move
            else:
                move = numbers_candies
                print(f'\nБот забирает {move} конфет!')
                return move
        case 3:
            if numbers_candies >= 28:
                move = numbers_candies % 29
                if move == 0:
                    move += 1
                print(f'\nБот забирает {move} конфет!') 
                return move
            else:
                move = numbers_candies
                print(f'\nБот забирает {move} конфет!') 
                return move

def game (game_mode:int) -> None:
    move = 1
    player_candies = [0,0]
    total_candies = int(2021)
    player = random.randint(1,2)
    match game_mode:
        case 1:
            print(f'\n Рандом решил, что первый ходит игорк {player}.')
        case 2:
            if player == 1:
                print('\n Рандом решил, что первый ход Пользователя.')
            else:
                print('\n Рандом решил, что первый ход Бота.')
        case 3:
            if player == 1:
                print('\n Рандом решил, что первый ход Пользователя.')
            else:
                print('\n Рандом решил, что первый ход AI.')
    while total_candies > 0:
        print(f'\nХод {move}. \nНа столе осталось {total_candies} конфет!') 
        match game_mode:
            case 1:
                print(f'\nУ игрока 1: {player_candies[0]} конфет \nУ игрока 2: {player_candies[1]} конфет')
            case 2:
                print(f'\nУ Вас: {player_candies[0]} конфет \nУ бота: {player_candies[1]} конфет')
            case 3:
                print(f'\nУ Вас: {player_candies[0]} конфет \nУ сверхразума: {player_candies[1]} конфет')
    
        if (player == 1): 
                candies = player_move(1, total_candies, game_mode = 1) 
                player_candies[0] += candies 
                total_candies -= candies 
                player = 2
        else:
            match game_mode:
                case 1: 
                    candies = player_move(2, total_candies, game_mode = 1) 
                case 2: 
                    candies = player_move(2, total_candies, game_mode = 2) 
                case 3: 
                    candies = player_move(2, total_candies, game_mode = 3) 
            player_candies[1] += candies 
            total_candies -= candies 
            player = 1
        move+=1
    match game_mode: 
        case 1: 
            if (player == 2): 
                print(f'\nВыиграл игрок 1, и он забирает все конфеты!\n') 
            else:  
                print(f'\nВыиграл игрок 2, и он забирает все конфеты!\n') 
        case 2: 
            if (player == 2): 
                print(f'\nВы выиграли и забираете все конфеты!\n') 
            else:  
                print(f'\nВыиграл Бот, и он забирает все конфеты!\n')
        case 3: 
            if (player == 2): 
                print(f'\nВы выиграли и забираете все конфеты!\n') 
            else:  
                print(f'\nВыиграл AI, и он забирает все конфеты!\n') 

print(f'\nДобро пожаловать в игру 2021 конфета!' 
        '\nВыберите режим игры:' 
        '\n1: Игра против Игрока' 
        '\n2: Игра против Бота' 
        '\n3: Игра против AI') 
check_select = False 
while not check_select: 
    select_mode = input(f'\nВведите номер режима: ') 
    match select_mode: 
        case '1':  
            print(f'Выбрана игра против Игрока!') 
            game(int(select_mode)) 
            check_select = True 
        case '2':  
            print(f'Выбрана игра против Бота!') 
            game(int(select_mode)) 
            check_select = True 
        case '3':  
            print(f'Выбрана игра против AI!') 
            game(int(select_mode)) 
            check_select = True 
    if (select_mode != '1') and (select_mode != '2') and (select_mode != '3'): 
        print('\nВы ввели неверные данные, попробуйте снова!')
    

            
