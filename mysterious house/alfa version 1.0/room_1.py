from random import randint
import sys
def room_1():
    print('''Вы появились в таинственном доме.
    Чтобы покинуть его необходимо пройти 6 комнат.''')
    print('Вы вошли в первую комнату ')
    print('''Перед вами четыре двери, и только с помощью двух вы сможете пройти дальше.
За одной из дверей сидит голодный медведь, за другой помещение, заполненное ядовитым газом, а за двумя другими дверьми проход в следующую комнату.''')

    a = int(input('Выберите номер двери от одного до четырёх  '))
    if a > 4 or a < 1:
        print('Внимательнее читай правила!!!')
        return room_1()
    dice = randint(1,4)
    if dice == 1:
        print('Ты умер от яда...')
        sys.exit()
    if dice == 2:
        print('Тебе съел медведь...')

        sys.exit()
    if dice == 3:
        print('Ты выжил и прошёл во вторую комнату!')

    if dice == 4:
        print('Ты выжил и прошёл во вторую комнату!')
