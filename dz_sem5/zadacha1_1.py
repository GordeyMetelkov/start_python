from random import randint
def start(counter: int, start_player: str, player: str, comp: str) -> int:
    if start_player == player: return counter%2==0
    else: return counter%2==1
konfet = 23
counter = 0
max_value = 4
player1 = input("Имя игрока:")
player2 = 'Супермозг'
players = [player1, player2]
start_player = players[randint(0,1)]
print(f"Начинает {start_player}")
print()
print((f"На столе {konfet} конфет."))
print()
while konfet!=0:
    if start(counter, start_player, player1, player2):
        print(f"Ход игрока {player1}")
        hod = int(input("Сколько конфет отнять? - > "))
        print()    
        while hod > max_value or hod <= 0 or hod > konfet:
            print(f"Недопустимое количество, отнимите от 1 до {max_value} конфет!")
            print()
            hod = int(input("Сколько конфет отнять? - > "))
        else:
            konfet-=hod
            lasthod = hod
            if konfet == 0:
                print(f"Победил {player1}")
                print()
            else:
                counter+=1
                print(f'Осталось {konfet} конфет.')
                print()
    else:
        print(f"Ход игрока {player2}")
        if counter==0:
            hod = konfet%max_value
        elif counter == 1:
            if konfet%max_value==0:hod = max_value
            elif lasthod < konfet%max_value:
                hod = konfet%max_value - lasthod
            elif lasthod == max_value:
                hod = konfet%max_value
        else:
            if konfet < max_value:
                hod = konfet
            elif konfet == max_value*2+1: 
                hod = max_value
            elif konfet <= 3*max_value and konfet > max_value*2:
                hod = konfet-(max_value*2+2)
            elif konfet <= max_value*2:
                hod = konfet - (max_value + 1)
            elif lasthod == max_value:
                hod = max_value
            else: hod = max_value - lasthod
        if hod==0: hod+=1
        konfet-=hod
        counter+=1
        print(f"Я отнимаю {hod} конфет")
        print()
        print(f"Осталось {konfet} конфет")
        print()
        if konfet == 0: print("Я победил")