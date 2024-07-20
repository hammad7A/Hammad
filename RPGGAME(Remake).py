import random
print("You have special abilites: ")
print("1.GenocideCutter 2.GalaxySlam")
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
    6: {'name': last_player_name, 'hp': 15000, 'damage': random.randint(500, 600)},
    'special_pl':{'damage_two':random.randint(2000,4500)},
    'special_two_pl':{'damage_three':random.randint(2500,4550)}


}

enemy = {
    1: {'name': enemy_name, 'hp': 50, 'damage': 5},
    2: {'name': enemy_name, 'hp': 60, 'damage': 9},
    3: {'name': enemy_name, 'hp': 75, 'damage': 15},
    4: {'name': enemy_name, 'hp': 80, 'damage': 15},
    5: {'name': enemy_name, 'hp': 100, 'damage': 20},
    6: {'name': last_name_enemy, 'hp': 20000, 'damage': random.randint(150, 325)},
    'special_en':{'damage_two':random.randint(2500,3000)},
    'special_two_en':{'damage_three':random.randint(1500,3500)}


}


def main(player_s: dict, enemy_s: dict):
    for i in range(1, 7):
        print(f"This is level {i} Battle ")
        while enemy[i]['hp'] > 0:
            attack_choice = input("Enter '1' to attack or enter the name of your special ability:  ").lower()
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
                        if random.randint(0, 100) <= 25:
                            vortex_damage = enemy['special_en']['damage_two']
                            player[i]['hp'] -= vortex_damage
                            print('VIMUSER: VORTEX BLAST!!!')
                        elif random.randint(0, 500) <= 25:
                            dragon_damage = enemy['special_two_en']['damage_three']
                            player[i]['hp'] -= dragon_damage
                            print('VIMUSER: DRAGONS CLAW!!!')
                        if attack_choice == 'GenocideCutter':
                            genocide_damage = player['special_pl']['damage_two']
                            enemy[i]['hp'] -= genocide_damage
                            print(f"{player_name}: GENOCIDE CUTTER!!!")
                        elif attack_choice == 'GalaxySlam':
                            slam_damage = player['special_two_pl']['damage_three']
                            enemy[i]['hp'] -= slam_damage
                            print(f"{player_name}: GALAXY SLAM!!!")
                        player_buff = attack_damage + 500
                        enemy_buff = goblin_damage + 175
                        enemy[i]['hp'] -= player_buff
                        player[i]['hp'] -= enemy_buff
                        print(f"VimUser has {enemy[i]['hp']} hp left! ")
                        print(f"You have {player[i]['hp']} hp left! ")
                    if player[i]['hp'] < 0:
                        print(f"You lost! ")
                        return player
                    else:
                        if enemy[i]['hp'] < 0:
                            print(f"Congrats! You have defeated VimUser! ")
                            return enemy


main(player, enemy)
