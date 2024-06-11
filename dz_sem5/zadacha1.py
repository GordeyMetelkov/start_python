def winner(counter: int, player1: str, player2: str) -> str:
    if counter % 2 == 0:
        return player1
    else:
        return player2
konfet = 28
counter = 0
max_value = 3
player1 = input("Имя игрока 1:")
player2 = input("Имя игрока 2:")
print()
print((f"На столе {konfet} конфет. Ход игрока {player1}"))
print()
while konfet != 0:
    hod = int(input("Сколько конфет отнять? - > "))
    print()    
    while hod > max_value or hod <= 0 or hod > konfet:
        print(f"Недопустимое количество, отнимите от 1 до {max_value} конфет!")
        print()
        hod = int(input("Сколько конфет отнять? - > "))
    else:
        konfet -= hod
        if konfet == 0:
            print(f"Победил {winner(counter, player1, player2)}")
            print()
        else:
            counter+=1
            print(f'Осталось {konfet} конфет. Ход игока {winner(counter, player1, player2)}')
            print()


