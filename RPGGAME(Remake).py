import random

Arcana = 750
Energon = 500

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

print(f"{RED}You have special abilities: ")
print(f"{RED}1. GenocideCutter 2. GalaxySlam")

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
}

enemy = {
    1: {'name': enemy_name, 'hp': 50, 'damage': 5},
    2: {'name': enemy_name, 'hp': 60, 'damage': 9},
    3: {'name': enemy_name, 'hp': 75, 'damage': 15},
    4: {'name': enemy_name, 'hp': 80, 'damage': 15},
    5: {'name': enemy_name, 'hp': 100, 'damage': 20},
}


special_en_hp = {'name': last_name_enemy, 'hp': 20000}
special_pl_hp = {'name': last_player_name, 'hp': 15000}


def main(player_s: dict, enemy_s: dict):
    for i in range(1, 6):
        print(f"{MAGENTA}This is level {i} Battle ")
        while enemy[i]['hp'] > 0:
            attack_choice = input(f"{GREEN}Enter '1' to attack: ").lower()
            if attack_choice == '1':
                attack_damage = player[i]['damage']
                enemy[i]['hp'] -= attack_damage
                goblin_damage = enemy[i]['damage']
                player[i]['hp'] -= goblin_damage
            if enemy[i]['hp'] > 0:
                print(f"{RED}The enemy has {enemy[i]['hp']} hp left ")
                print(f"{YELLOW}You have {player[i]['hp']} hp left ")
                if i > 5:
                    print(f"You have defeated {enemy[i]['name']} enemy! ")
                    return enemy

def boss_level(pl: dict, en: dict):
    global Energon
    global Arcana
    for i in range(6,7):
        while True:
            attack_boss = input(f"{BLUE}Enter '1' to attack or use your special abilites: ").lower()
            if attack_boss == '1':
                attack_damage = random.randint(350,700)
                special_en_hp['hp'] -= attack_damage
                enemy_damage = random.randint(0,1000)
                special_pl_hp['hp'] -= enemy_damage
            elif attack_boss == 'genocidecutter':
                if Energon >= 250:
                    Energon -= 250
                    attack_damage_two = random.randint(1500,4000)
                    special_en_hp['hp'] -= attack_damage_two
                    print(f"{YELLOW}{last_player_name}:GENOCIDE CUTTER!!!")
                    print(f"Energon:{Energon}")
                else:
                    print(f"Not enough energon! ")
                if random.randint(0,100) < 35:
                    if Arcana >= 250:
                        Arcana -= 250
                        attack_enemy_three = random.randint(0,6000)
                        special_pl_hp['hp'] -= attack_enemy_three
                        print(f"{MAGENTA}{last_name_enemy}:DRAGON CLAW!!!")
                        print(f"Arcana:{Arcana}")
                else:
                    option_lasts_two = random.randint(100,650)
                    special_pl_hp['hp'] -= option_lasts_two
            elif attack_boss == 'galaxyslam':
                if Energon >= 250:
                    Energon -= 250
                    attack_player_three = random.randint(0,5000)
                    special_en_hp['hp'] -= attack_player_three
                    print(f"{YELLOW}{last_player_name}:GALAXY SLAM!!!")
                    print(f"Energon:{Energon}")
                else:
                    print(f"Not enough energon! ")
                if random.randint(0,50) < 5:
                    if Arcana >= 250:
                        Arcana -= 250
                        attackers_enemy = random.randint(2250,5000)
                        special_pl_hp['hp'] -= attackers_enemy
                        print(f"{MAGENTA}{last_name_enemy}:HAILSTORM!!!")
                        print(f"Arcana:{Arcana}")
                else:
                    option_lasts_enemy = random.randint(150,500)
                    special_pl_hp['hp'] -= option_lasts_enemy

            if special_en_hp['hp'] > 0:
                print(f"{RED}The enemy has {special_en_hp['hp']}hp! ")
                print(f"{YELLOW}You have {special_pl_hp['hp']}hp! ")
            if special_en_hp['hp'] < 0:
                return special_en_hp

main(player, enemy)
boss_level(player,enemy)


main(player, enemy)
