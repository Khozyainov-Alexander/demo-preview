import random
def room_6():
    print("*****************************")
    print('Ты попал в последниию комнату')
    print('Чтобы выбраться тебе нужно выбрать одну из дверей, у которой замок такой же как и ключ.')
    print("если выберешь правильную дверь, сможешь выбраться из этого особняка.")
    print("либо же останешься здесь навсегда!")
    shapes = ['квадратный', 'круглый', 'треугольный']
    key = random.choice(shapes)
    print(f'Тип ключа: {key}')
    doors = [1, 2, 3]
    random.shuffle(shapes)
    door_locks = dict(zip(doors, shapes))
    for attempt in range(2):
        door_choice = int(input("Выберите дверь (от 1 до 3): "))
        if door_choice < 1 or door_choice > 3:
            print("Некорректный выбор двери. Попробуйте снова.")
            continue
        door_lock = door_locks[door_choice]
        print(f"Форма замка за дверью {door_choice}: {door_lock}.")
        if door_lock == key:
            print("Замок открыт! ")
            print("ты прошёл все испытания и покинул таинственный дом, молодец!")
            return
        else:
            print("Замок не подходит.")
    print("Ты исчерпал все попытки...")
    print("Ты застрял здесь навсегда!")
