import random
import sys
def room_2():
    print("*****************************")
    print('Вы вошли во вторую комнату. ')
    print('''Вам нужно угадать пароль, состоящий из 3 символов.
В пароле могут присутствовать цифры 1,2,3. Цифры в комбинации не могут повторяться. У вас будет 3 попытки.
Если ты не угадаешь пароль на тебя упадёт пианино.''')


    secret_combination = random.sample(range(1, 4), 3)
    attempts = 4

    while attempts > 0:
        while True:
            guess = input("Введите комбинацию из трех чисел от 1 до 3 через пробел: ")
            user_combination = [int(x) for x in guess.split()]
            if len(set(user_combination)) == 3 and all(1 <= num <= 3 for num in user_combination):
                break
            else:
                print("Некорректный ввод. Числа должны быть от 1 до 3 и не должны повторяться.")
                print('На тебя упало пианино... Надо было внимательнее читать правила!!!')

                sys.exit()


        if user_combination == secret_combination:
            print('''Поздравляем, вы угадали комбинацию!
Вы выжили и прошли в третью комнату!''')
            break
        else:
            print("Вы не угадали комбинацию. У вас осталось", attempts - 1, "попыток.")
            attempts -= 1

    if attempts == 0:
        print("На вас упало пианино... Загаданная комбинация была", secret_combination)
        sys.exit()
