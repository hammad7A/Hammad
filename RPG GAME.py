#First make the player's dictionary containing health name and inventory
#I will make an attack pattern for the player
#Then I will have a goblin attack the player
#The player will take damage
#And his health will get less but he will defeat goblin!
import random
player_name = input("Enter your name ")
enemy_name = "goblin"

levels = {1:{'name':player_name,'hp':100},2:{'name':player_name,'hp':125}
,3:{'name':player_name,'hp':130},4:{'name':player_name,'hp':150},5:{'name':player_name,'hp':160}}
levels_enemy = {1:{'name':enemy_name,'hp':50},2:{'name':enemy_name,'hp':60},
3:{'name':enemy_name,'hp':60},4:{'name':enemy_name,'hp':75},5:{'name':enemy_name,'hp':100}}

def level_one():
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            attack_damage = 7
            levels_enemy[1]["hp"] -= attack_damage
            goblin_damage = 5
            levels[1]['hp'] -= goblin_damage
            print(levels_enemy[1])
            print(levels[1])
            if levels_enemy[1]['hp'] < 0:
                print(f"You have defeated {levels_enemy[1]['name']} successfully! ")
                print(f"You have passed level one and now you can now move onto level 2! ")
                return levels_enemy[1]
def level_two():
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            attack_damage = 8
            levels_enemy[2]['hp'] -= attack_damage
            goblin_damage = random.randint(0,15)
            levels[2]['hp'] -= goblin_damage
            print(levels_enemy[2])
            print(levels[2])
            if levels_enemy[2]['hp'] < 0:
                print(f"You have defeated {levels_enemy[2]['name']} successfully! ")
                print(f"You have passed level two and you can now move onto level 3")
                return levels_enemy[2]
def level_three():
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            attack_damage = 10
            levels_enemy[3]['hp'] -= attack_damage
            goblin_damage = random.randint(5,20)
            levels[3]['hp'] -= goblin_damage
            print(levels_enemy[3])
            print(levels[3])
            if levels_enemy[3]['hp'] < 0:
                print(f"You have defeated {levels_enemy[2]['name']} successfully! ")
                print(f"You have passed level two and you can now move onto level 4")
                return levels_enemy[3]
def level_four():
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            attack_damage = 13
            levels_enemy[4]['hp'] -= attack_damage
            goblin_damage = random.randint(8,25)
            levels[4]['hp'] -= goblin_damage
            print(levels_enemy[4])
            print(levels[4])
            if levels_enemy[4]['hp'] < 0:
                print(f"You have defeated {levels_enemy[2]['name']} successfully! ")
                print(f"You have passed level two and you can now move onto level 5")
                return levels_enemy[4]
def level_five():
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            attack_damage = 15
            levels_enemy[5]['hp'] -= attack_damage
            goblin_damage = random.randint(10,30)
            levels[5]['hp'] -= goblin_damage
            print(levels_enemy[5])
            print(levels[5])
            if levels_enemy[5]['hp'] < 0:
                print(f"You have defeated {levels_enemy[2]['name']} successfully! ")
                print(f"Congrats! You have completed the game! ")
                return levels_enemy[5]
level_one()
level_two()
level_three()
level_four()
level_five()