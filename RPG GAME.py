import random

player_name = input("Enter your name: ")
last_player_name = 'Gri'
enemy_name = 'Goblin'
last_name_enemy = 'VimUser'
player = {
    1: {'name': player_name, 'hp': 100, 'damage': 10},
    2: {'name': player_name, 'hp': 100, 'damage': 12},
    3: {'name': player_name, 'hp': 125, 'damage': 15},
    4: {'name': player_name, 'hp': 130, 'damage': 20},
    5: {'name': player_name, 'hp': 150, 'damage': 25},
    6: {'name': last_player_name, 'hp': 3000, 'damage': random.randint(500, 600)}
}

enemy = {
    1: {'name': enemy_name, 'hp': 50, 'damage': 5},
    2: {'name': enemy_name, 'hp': 60, 'damage': 9},
    3: {'name': enemy_name, 'hp': 75, 'damage': 15},
    4: {'name': enemy_name, 'hp': 80, 'damage': 15},
    5: {'name': enemy_name, 'hp': 100, 'damage': 20},
    6: {'name': last_name_enemy, 'hp': 5000, 'damage': random.randint(150, 325)}
}


def main(player: dict, enemy: dict):
    for i in range(1, 7):
        print(f"This is level {i} Battle ")
        while enemy[i]['hp'] > 0:
            attack_choice = input("Enter '1' to attack: ")
            if attack_choice != '1':
                print("Please press '1' to attack: ")
            if attack_choice == '1':
                attack_damage = player[i]['damage']
                enemy[i]['hp'] -= attack_damage
                goblin_damage = enemy[i]['damage']
                player[i]['hp'] -= goblin_damage

                if enemy[i]['hp'] > 0:
                    print(f"The enemy has {enemy[i]['hp']} hp left ")
                    print(f"You have {player[i]['hp']} hp left ")
                    if i == 5:
                        print(f"You have defeated {enemy[i]['name']} enemy! ")
                    if i == 6:
                        player_buff = attack_damage + 150
                        enemy_buff = goblin_damage + 175
                        enemy[i]['hp'] -= player_buff
                        player[i]['hp'] -= enemy_buff
                        print(f"VimUser has {enemy[i]['hp']} hp left! ")
                        print(f"You have {player[i]['hp']} hp left! ")
                    if player[i]['hp'] < 0:
                        print(f"You lost! ")
                    else:
                        if enemy[i]['hp'] < 0:
                            print(f"Congrats! You defeated the enemy! ")


main(player, enemy)
