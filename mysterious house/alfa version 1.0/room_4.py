import sys
import random
def room_4():
    print("*****************************")
    print('Ты вошёл в четвёртую комнату.')
    print('В ней сидит тролль.')
    print('Чтобы пройти дальше вам нужно выиграть его в камень, ножницы, бумага.')
    print("Игра будет идти до трёх побед")
    print('Если ты проиграешь, тролль раздавит вас своей дубинкой... Удачи!')

    options = ["камень", "ножницы", "бумага"]

    user_points = 0
    computer_points = 0

    while user_points < 3 and computer_points < 3:
        user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
        computer_choice = random.choice(options)
        print("Тролль выбрал:", computer_choice)
        if user_choice in options:
            if user_choice == computer_choice:
                print("Ничья!")
            elif (
                    (user_choice == "камень" and computer_choice == "ножницы")
                    or (user_choice == "ножницы" and computer_choice == "бумага")
                    or (user_choice == "бумага" and computer_choice == "камень")
            ):
                print("Вы выиграли раунд! Ваш счёт", user_points + 1, ';', 'Cчёт тролля', computer_points)
                user_points += 1
            else:
                print("Ты проиграл раунд!  Ваш счёт", user_points, ';', 'Cчёт тролля', computer_points + 1)
                computer_points += 1
        else:
            print("Некорректный ввод. Попробуйте еще раз.")
    print("Конец игры!")
    if user_points > computer_points:
        print("Ты победил!")
        print('Ты выжил и прошёл в пятую комнату ')
    else:
        print("Тролль победил!")
        print('Тролль расплющил тебя дубинкой...')
        sys.exit()
