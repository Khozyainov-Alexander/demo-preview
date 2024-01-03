import random
import sys
def room_5():
    print("*****************************")
    print('Ты вошёл в пятую комнату.')
    print('Тебе нужно выиграть Свирепого Бобра в игре Ним.')
    print("В этой игре ты будешь по очереди со Свирепым Бобром брать шарики от 1 до 4.")
    print('Выиграет тот, кто заберёт шарики последним.')
    print("Если ты выиграешь, то пройдёшь в следующую комнату, если проиграешь бобёр сгрызёт тебя, как древесину.")
    balls = 20
    while balls > 0:
        while True:
            try:
                player_choice = int(input(f"Сколько шариков вы хотите взять? (от 1 до 4) Шариков осталось: {balls}  "))
                if player_choice < 1 or player_choice > 4 or player_choice > balls:
                    print("Некорректный ввод. Попробуйте снова.")
                else:
                    balls -= player_choice
                    break
            except ValueError:
                print("Ошибка! Введите целое число.")
        if balls <= 0:
            print(f"Ты забрал последний шарик, Игра окончена. Поздравляем!")
            print('Ты выиграл и прошёл в шестую комнату!')
            break
        print(f"Шариков осталось: {balls}")
        computer_choice = random.randint(1, min(balls, 4))
        balls -= computer_choice
        print(f"Свирепый Бобрёр взял {computer_choice}. Шариков осталось: {balls}")
        if balls <= 0:
            print("Свирепый Бобрёр забрал последний шарик, Игра окончена. Свирепый Бобрёр выиграл!")
            print('Тебя бобёр загрыз до смерти...')
            sys.exit()
