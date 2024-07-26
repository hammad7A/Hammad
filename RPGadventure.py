import random,sys
import time

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
def main():
    print(f"{RED}Welcome to the Gricane world")
    print(f"You can only take/use 1 item from a door so choose wisely! ")
    print(f"You can never come back to the door you are out of once! ")
    print(f"You have MalevolentShrine and BeastChiller special attacks")
    print(f"Type faster to have chances of doing more damage! ")
    player_health = 200
    player_inventory = []
    player_power = random.randint(5,11)
    player_intelligence = 0
    goblin_damage = random.randint(2, 24)
    goblin_health = 300
    healing_potion = 500
    first_boss = {"Name":"Vindicator","Health":1000,"GalaxySlam":random.randint(55,90),
                  "HellWave":random.randint(65,145)}
    second_boss = {"Name":"KingSlayer","Health":5000,"IceAbyss":random.randint(0,2),
                   "CelestialBlow":random.randint(0,2)}
    third_dungeon_eiser = {"Name":"Eiser","Health":3500,"SoulShatter":random.randint(0,2),
                           "VoidRend":random.randint(0,2)}
    third_boss = {"Name":"Roufa,DevourerofPoison","Health":15000,"CleaverVeil":random.randint(300,700),
                  "ImperialDirge":random.randint(150,800)}
    fourth_boss = {"Name":"TheFlameTyrant","Health":35000,"ShadowSlice":random.randint(0,2),
                   "DivineWrath":random.randint(0,2)}
    final_boss = {"Name":"AbyssalReaper","Health":100000,"VoidSlash":random.randint(0,2),
                  "SpectralScythe":random.randint(0,2)}
    door1 = {'Name': "FeyVeilGate", "Items": {"MagicRing", "Flask","RuggedPhilter"}}
    door2 = {'Name': "EnigmaGate", "Items": ["MithrilBracers", "KeyofLight"]}
    door3 = {'Name': "EtherealGate", "Items": ["Gristal", "TitanStrength"]}
    doors = {1: door1, 2: door2, 3: door3}
    return player_intelligence, player_inventory, goblin_health, player_health, player_power, goblin_damage,first_boss,second_boss,healing_potion,third_boss,third_dungeon_eiser,fourth_boss,final_boss

def first_dungeon(player_intelligence, player_inventory, goblin_health, player_health, player_power, goblin_damage,first_boss):
    MagicRing = random.randint(25,40)
    flask = random.randint(50,115)
    door1 = {'Name':"FeyVeilGate","Items":{'MagicRing':MagicRing,'Flask':flask}}
    print(f"{CYAN}You have the following things: {door1}")
    items_choice = input(f"{BLUE}Enter the name of the item you want to use: 'n' if you don't want to use anyhting: ")
    if items_choice == 'MagicRing':
        player_power += MagicRing
        print(f"Current Power {player_power} Current Health {player_health}")
    elif items_choice == 'Flask':
        player_health += flask
        print(f"Your current health is {player_health}")
    elif items_choice == 'n':
        pass
    while goblin_health > 0:
        attack_choice = input(f"Enemies are attacking you!!!Press '1' to attack them: ")
        if attack_choice == '1':
            start_time = time.time()
            typing_speed = 1 / (time.time() - start_time) if (time.time() - start_time) != 0 else 1
            player_powers = random.randint(5,10)
            goblin_damage = random.randint(2,14)
            player_powers += MagicRing
            goblin_health -= player_powers
            player_health -= goblin_damage


            print(f"Your health is {player_health}")
            print(f"The enemy's health is {goblin_health}")
            if goblin_health < 0:
                print(f"You have defeated the enemy! You got an {RED}Etheral Ring!  ")
                print(f"{BLUE}Etheral ring will give you PERMANENT hp! ")
                EtheralRing = 650
                player_inventory.append(f"EtheralRing:{EtheralRing}")
                print(player_inventory)
                use_item = input(f"{RED}Do you want to use Etheral Ring: y/n ")

                if use_item == 'y':
                    player_health += EtheralRing
                    print(f"{RED}Your current health now is {player_health} ")

                if typing_speed < 2.0:
                    damage_modifier = 1.5
                elif typing_speed <= 1.2:
                    damage_modifier = 1.2
                else:
                    damage_modifier = 1.0
                if goblin_health < 0:
                    print(f"{MAGENTA}Walking slowly...footsteps of some identity increasing...")
                    time.sleep(2)
                    print(f"{MAGENTA}Vindicator: You will not see the daylight...I shall slaughter you for good! ")

                elif player_health < 0:
                    print("You lost! ")
                    sys.exit()
                
                BeastChiller = 0
                MalevolentShrine = 0
                while first_boss['Health'] > 0:
                    start_time = time.time()
                    attack_boss = input(f"{BLUE}Enter the name of your abilitys to attack: ").lower()
                    end_time = time.time()
                    if attack_boss == 'malevolentshrine':
                        if typing_speed >= 2.0:
                            MalevolentShrine = random.randint(35,120) * damage_modifier
                        elif typing_speed  <= 1.2:
                            MalevolentShrine = random.randint(50, 80) * damage_modifier
                        first_boss['GalaxySlam'] = random.randint(85, 95)

                        print(f"{RED}Gri: {YELLOW}Domain Expansion: Malevolent Shrine")
                        print(f"{RED}Vindicator: {YELLOW}GALAXY SLAM!!!")
                        first_boss['Health'] -= MalevolentShrine

                        player_health -= first_boss['GalaxySlam']
                        print(f"{BLUE}You dealth {MalevolentShrine} damage to the boss! He now has {RED}{first_boss['Health']} hp left!  ")
                        print(f"{BLUE}The boss dealt {first_boss['GalaxySlam']} damage to you! You now have {RED}{player_health} hp left")

                    elif attack_boss == 'beastchiller':
                        if typing_speed >= 2.0:
                            BeastChiller = random.randint(45,100) * damage_modifier
                        elif typing_speed <= 1.2:
                            BeastChiller = random.randint(50, 90) * damage_modifier
                        print(f"{RED}Gri: {YELLOW}BEAST CHILLER!!!")
                        print(f"{RED}Vindicator: {YELLOW}HELLWAVE!!!")
                        first_boss['HellWave'] = random.randint(65, 70)
                        first_boss['Health'] -= BeastChiller
                        player_health -= first_boss['HellWave']


                        print(f"{BLUE}You dealth {BeastChiller} damage to the boss! He now has {RED}{first_boss['Health']} hp left!  ")
                        print(f"{BLUE}The boss dealt {first_boss['HellWave']} damage to you! You now have {RED}{player_health} hp left")
                    if first_boss['Health'] <= 0:
                        print(f"You defeated Vindicator! ")

                    elif player_health <= 0:
                        print(f"You lost! ")
                        sys.exit()
                    elif first_boss['Health'] > 0 and player_health <= 0:
                        print(f"{RED}Warriors..You lost!")
                        sys.exit()
    return player_intelligence,player_inventory,MalevolentShrine,BeastChiller,typing_speed,damage_modifier,goblin_health,player_health,player_powers,goblin_damage

def second_dungeon(player_intelligence, player_inventory, MalevolentShrine, BeastChiller, typing_speed, damage_modifier, player_health, player_power,second_boss,healing_potion):
    print(f"Your current hp right now is {player_health}")
    door2 = {'Name': "EnigmaGate", "Items": ["MithrilBracers", "KeyofLight"]}
    print(f"{CYAN}You have the following things{door2['Items']}")
    MithrilBracers_power = 200
    MithrilBracers_health = 500
    KeyofLight = 10
    print(f"{MAGENTA}Carol: Hey who are you? ")
    time.sleep(2)
    print(f"Gri: I am gri...a lost warrior in this dungeon! ")
    time.sleep(2)
    print(f"Saad: Ah same...we should  fight together")
    time.sleep(2)
    print(f"Gri: Yeah sure let's do! ")
    time.sleep(2)
    print(f"Saad: That in your hand is the key of light..it buffs your magic damage and also grants physical damage")
    time.sleep(2)
    print(f"Saad: However to get the physical damage you need the intelligence above a certain level and it's not easy! ")
    time.sleep(2)
    player_intelligence += KeyofLight
    print(f"Your current intelligence is now {RED}{player_intelligence} ")
    MalevolentShrine += KeyofLight
    BeastChiller += KeyofLight
    time.sleep(2)
    print(f"Your magic attacks have been buffed! ")
    time.sleep(2)
    print(f"Saad: Gri we got company here..let's do this! ")
    goblin_health = 100
    while True:
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            player_power = random.randint(15,25)
            goblin_damage = random.randint(15,30)
            print(goblin_health)
            goblin_health -= player_power
            player_health -= goblin_damage
            print(f"{BLUE}You did {player_power} damage to enemy. His hp is now {goblin_health} hp ")
            print(f"The enemy did {goblin_damage} damage to you and your hp is now {player_health} hp")
            if goblin_health <= 0:
                print(f"You defeated the enemy! ")
                break
            elif player_health <= 0:
                print(f"{CYAN}You lost but Carol saved your ass! ")
                break
    Carol_Health = 500
    Carol_Special_name = "Ultimate Maelstrom"
    Carol_Attack = random.randint(575,800)
    print(f"Saad: That was quite a sudden attack..Gri you alright? \n")
    time.sleep(2)
    print(f"Gri: Yeah I am fine, let's move! ")
    time.sleep(2)
    print(f"You feel your strength increasing as the mithril bracers take effect...\n")
    player_power += MithrilBracers_power
    print(f"Your current power is now {CYAN}{player_power} ")
    player_health += MithrilBracers_health
    print(f"Your current hp is now {CYAN}{player_health} ")
    player_power += MalevolentShrine
    time.sleep(2)
    print(f"{BLUE}The walls suddenly blow up...Out of the dust comes the {RED}KingSlayer..\n")
    time.sleep(2)
    print(f"Saad: GRI SPLIT! WE WILL ATTACK HIM FROM TWO SIDES\n")
    time.sleep(2)
    print(f"{MAGENTA}Saad suffers deadly blows..GRI RUN INTO THE TUNNEL WE ARE TOO WEAK!! \n")
    time.sleep(2)
    Carol_Health -= second_boss['IceAbyss']
    print(f"{BLUE}Saad's current hp is {Carol_Health}")
    time.sleep(2)
    print(f"Gri: Don't worry I will use MR to heal you..")
    Carol_Health += healing_potion
    print(f"Saad's current health is now {Carol_Health}")
    time.sleep(2)
    print(f"You good? Yeah ok let's move on we need to get away from that monster! ")
    time.sleep(2)
    print(f"They find a hidden dungeon inside a dungeon and go inside it..Encounter enemies! ")
    time.sleep(2)
    print(f"Your current hp is {player_health} ")
    goblin_health_hidden = 1000
    while True:
        
        goblin_damage_hidden = random.randint(215,300)
        attack_enemies = input("Press '1' to attack: ")
        if attack_enemies == '1':
            goblin_health_hidden -= player_power
            player_health -= goblin_damage_hidden
            print(f"You dealt {player_power} damage to the enemy. His current hp is {goblin_health_hidden} ")
            print(f"The enemy dealt {goblin_damage_hidden} damage to you. Your current hp is {player_health} ")
            if player_health <= 0:
                print(f"{RED}Gri: Carol..I took a direct hit.You gotta handle him")
                print(f"Saad: Yeah leave it to me! ")
                goblin_health_hidden -= Carol_Attack
                Carol_Health -= goblin_damage_hidden
                print(f"{YELLOW}Carol dealt {Carol_Attack} damage to the enemy. The enemy's current hp is {goblin_health_hidden} ")
                print(f"{YELLOW}The enemy dealt {goblin_damage_hidden} damage to Carol. Carol's current hp is {Carol_Health} ")
                if goblin_health_hidden < 0:
                    print(f"Phew that was close..Gri you fine?")
                    time.sleep(2)
                    print(f"Gri: Yeah I am fine")
                time.sleep(2)
                print(f"Gri: Hey..What are these 2 glowing things? ")
                time.sleep(2)
                print(f"Saad: This is...{RED}The Elixirs of Serpents.")
                time.sleep(2)
                print(f"If one consumes it they are said to get powers beyond imaginations..")
                time.sleep(2)
                print(f"Gri: I don't know it's side effects but we should consume it if we want to beat up that boss..")

                elixir_choice = input("Do you want to drink the potion: y/n ")
                elixer_power = 150
                elixer_health = 3000
                if elixir_choice == 'y':
                    elixer_power += MalevolentShrine
                    elixer_power += BeastChiller
                    player_health += elixer_health
                    print(f"You feel overwhelming energy which your body can barely handle..")
                    break
    print(f"Gri: You find the door and I will kick his ass, Saad")
    while second_boss['Health'] > 0:
        start_time = time.time()
        attack_boss = input(f"{YELLOW}Enter the name of your abilities to attack: ").lower()
        end_time = time.time()
        if attack_boss == 'malevolentshrine':
            boss_random_two = random.randint(250, 400)
            MalevolentShrine = random.randint(200,625)
            MalevolentShrine += elixer_power
            second_boss['Health'] -= MalevolentShrine
            second_boss['CelestialBlow'] = min(second_boss['CelestialBlow'],400)
            player_health -= second_boss['CelestialBlow'] + boss_random_two
            print(f"{YELLOW}You dealt {MalevolentShrine} damage to KingSlayer. He now has {second_boss['Health']} hp left! ")
            print(f"{RED}KingSlayer dealth {second_boss['CelestialBlow']+boss_random_two} damage to you. You now have {player_health} hp left")
        elif attack_boss == 'beastchiller':
            boss_random_one = random.randint(120,500)

            BeastChiller = random.randint(125,500)
            BeastChiller += elixer_power

            second_boss['Health'] -= BeastChiller
            second_boss['IceAbyss'] = min(second_boss['IceAbyss'],550)
            player_health -= second_boss['IceAbyss'] + boss_random_one
            print(f"{YELLOW}You dealt {BeastChiller} damage to KingSlayer. He now has {second_boss['Health']} hp left! ")
            print(f"{RED}KingSlayer dealth {second_boss['IceAbyss']+boss_random_one} damage to you. You now have {player_health} hp left")
        if second_boss['Health'] <= 0:
            print(f"{YELLOW}You successfully defeated KingSlayer")
            break
        elif second_boss['Health'] > 0 and player_health <= 0:
            print(f"You lost..saad saved your ass! ")
            break
    return player_intelligence, player_inventory, MalevolentShrine, BeastChiller, typing_speed, damage_modifier, player_health, player_power,healing_potion,Carol_Health,Carol_Attack,Carol_Special_name
def third_dungeon(player_intelligence, player_inventory, MalevolentShrine, BeastChiller, typing_speed, damage_modifier, player_health, player_power,healing_potion,Carol_Health,Carol_Attack,Carol_Special_name,eiser):
    player_health += 2500
    print(f"{BLUE}Saad: Be careful I have heard that there is a Guardian of this dungeon somewhere..")
    time.sleep(2)
    print(f"Saad: He is known as the Guardian of Eiser")
    time.sleep(2)
    print(f"Gri: We better be careful..Do you want to face him? ")
    time.sleep(2)
    print(f"Saad: Yeah sure but first let's use MR on ourselves ")
    player_health += 1000
    Carol_Health += 750
    print(f"{RED}{MAGENTA}Your current hp is now {player_health} ")
    time.sleep(2)
    print(f"Saad's current hp is now {Carol_Health} ")
    time.sleep(2)
    print(f"{MAGENTA}...Gri: What is it Carol? ")
    time.sleep(2)
    print(f"Saad: Something worries me..the artifacts")
    time.sleep(2)
    print(f"Gri: Artifacts? What artifacts? ")
    time.sleep(2)
    print(f"Saad: That item we obtained..The Elixer of Serpents is a stage 1 artifact")
    time.sleep(2)
    print(f"There are 3 stages of artifacts and the higher the stage the stronger the artifact")
    time.sleep(2)
    print(f"Gri: What worries you though? ")
    time.sleep(2)
    print(f"Saad: If a stage 2 or 3 artifact gets in the wrong hands we are done for! ")
    time.sleep(2)
    print(f"Gri: How can we prevent that? Where are the artfifacts? ")
    time.sleep(2)
    print(f"The stage 2 artifact..The Amulet of Eryndor is located in the depths of this dungeon")
    time.sleep(2)
    print(f"Gri: Then let's go and grab it before it gets in the wrong hands ")
    time.sleep(2)
    print(f"Saad: Yeah but it won't be easy because that is where the Guardian of Eiser is ")
    time.sleep(2)
    print(f"The guardian guards the Eiser and about a thousand brave warriors have tried to get it but they were not worthy ")
    time.sleep(2)
    print(f"To obtain the Amulet of Eryndor is to risk your life..You have to make a sacred oath with the Guardian ")
    time.sleep(2)
    print(f"Gri: Sacred oath? What is that?")
    time.sleep(2)
    print(f"Saad: It's like making a deal and it depends on the Guardian that what kind of oath he makes with us ")
    time.sleep(2)
    print(f"Long ago there used to be a huge ring at the center of this dungeon and it had shards called Shards of Eternity ")
    time.sleep(2)
    print(f"Those shards were crushed to pieces by the strongest of all Abyssal Reaper..")
    time.sleep(2)
    print(f"Gri: Who is Abyssal Reaper? ")
    time.sleep(2)
    print(f"Saad: He is the strongest of all here and guards the shards of eternity..He could probably in our current state "
          f"kill us with just his pressure ")
    time.sleep(2)
    print(f"Gri: Well let's move and find that guardian ")
    time.sleep(2)
    print(f"Gri: I feel like someone is coming get ready")
    print(f"{RED} You..don't think you can steal the mighty amulet in my presence..BECAUSE MY NAME IS EISER ")
    while third_dung_eiser['Health'] > 0:
        start_time = time.time()
        attack_eiser = input(f"{RED}Enter the name of your abilities to attack: ").lower()
        end_time = time.time()
        if attack_eiser == 'malevolentshrine':
            if typing_speed >= 2.0:
                MalevolentShrine = random.randint(875,1250)
            elif typing_speed <= 2.0:
                MalevolentShrine = random.randint(690,1100)
            else:
                MalevolentShrine = random.randint(550,1100)
            boss_random_one = min(random.randint(50, 500), 500)
            third_dung_eiser['VoidRend'] += boss_random_one
            third_dung_eiser['Health'] -= MalevolentShrine
            third_dung_eiser['Health'] -= Carol_Attack
            player_health -= third_dung_eiser['VoidRend']
            print(f"{YELLOW}You dealt {MalevolentShrine} damage to Eiser . He now has {third_dung_eiser['Health']} hp left ")
            print(f"{RED}Eiser dealt {third_dung_eiser['VoidRend']} damage to you. You now have {player_health} hp left ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} to Eiser. Saad's hp is now {Carol_Health} ")
        elif attack_eiser == 'beastchiller':
            if attack_eiser == 'beastchiller':
                if typing_speed >= 2.0:
                    BeastChiller = random.randint(900, 1250)
                elif typing_speed <= 2.0:
                    BeastChiller = random.randint(875, 1100)
                else:
                    BeastChiller = random.randint(757, 1100)
            boss_random_two = min(random.randint(50, 500), 300)
            third_dung_eiser['SoulShatter'] += boss_random_two
            third_dung_eiser['Health'] -= BeastChiller
            player_health -= third_dung_eiser['SoulShatter']
            print(f"{YELLOW}You dealt {BeastChiller} damage to Eiser . He now has {third_dung_eiser['Health']} hp left ")
            print(f"{RED}Eiser dealt {third_dung_eiser['SoulShatter']} damage to you. You now have {player_health} hp left ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} to Eiser. Saad's hp is now {Carol_Health} ")
        if third_dung_eiser['Health'] <= 0:
            print(f"{MAGENTA}Thy strength is worthy of the Orbs of Eternity...")
            break
        elif player_health <= 0:
            print(f"You lost..warriors ")
            sys.exit()
        elif player_health <= 0 and third_dung_eiser['Health'] <= 0:
            print(f"You lost..warriors ")
            sys.exit()
    print(f"Gri: Saad you alright? ")
    time.sleep(2)
    print(f"Saad: Yeah I am fine lets take a look at the amulet ")
    time.sleep(2)
    print(f"Gri: Dam..it's beatiful..")
    time.sleep(2)
    print(f"Saad: We will both touch it with one hand so to get the powers ")
    time.sleep(2)
    print(f"Gri: Alright here we go ")
    time.sleep(2)
    print(f"{RED}You feel your abilites amplifying and surging with power ")
    amulet_hp = 3000
    player_health += amulet_hp
    Carol_Health += amulet_hp
    print(f"{BLUE}Your current hp is now {player_health} ")
    print(f"Saad's hp is now {Carol_Health} ")
    time.sleep(2)
    print(f"{BLUE}This-is unbelievable..This power")
    time.sleep(2)
    print(f"Saad: Told ya..it's a stage 2 artifact afterall ")
    time.sleep(2)
    print(f"Gri: It's so overwhelming I can feel it taking {RED}effect ")
    time.sleep(2)
    print(f"We should get some rest before fighting him ")
    time.sleep(2)
    print(f"OldSage: Oh..thy warriors are in luck..")
    time.sleep(2)
    print(f"Gri: The hell are you? What do you want? ")
    time.sleep(2)
    print(f"OldSage:When the moon turns red and the shadows lengthen, the true path will reveal itself to those who seek the light ")
    time.sleep(2)
    print(f"OldSage: I am the old sage..seeking the true vessel of the orbs of eternity ")
    time.sleep(2)
    print(f"Gri: Orbs of eternity? I have heard that name before ")
    time.sleep(2)
    print(f"Saad: That guardian we defeated said something about it ")
    time.sleep(2)
    print(f"OldSage: Oh you defeated him? Thy strength must be overwhelming ")
    time.sleep(2)
    print(f"Gri: Yeah we did..he was quite strong, saad pussied out *laughter* ")
    time.sleep(2)
    print(f"OldSage: I can take you where you want to go...to the fourth dungeon")
    time.sleep(2)
    print(f"But you have to defeat Roufa first ")
    time.sleep(2)
    print(f"Saad: You mean that beast..yeah right")
    time.sleep(2)
    print(f"Gri: ...")
    time.sleep(2)
    print(f"Saad: What is it? ")
    time.sleep(2)
    print(f"Something is weird..I don't know why but something is off ")
    time.sleep(2)
    print(f"Let's go..")
    time.sleep(2)
    print(f"The air grows still, heavy with a sinister chill. Shadows lengthen and dance as the walls tremble with an unseen force.")
    time.sleep(2)
    print(f"Then from the fire came Roufa, The Devourer of Poison ")
    time.sleep(2)
    print(f"Gri: LET'S DO THIS ")
    time.sleep(2)
    print(f"{RED}Your attacks have been changed...")
    print(f"{CYAN}Your attacks are now InfernalWrath and ChaosSurge")
    InfernalWrath = 0
    ChaosSurge = 0
    while third_boss['Health'] > 0:
        start_time = time.time()
        attack_boss = input(f"{RED}Enter the name of your abilites to attack: ").lower()
        end_time = time.time()
        if attack_boss == 'infernalwrath':
            if typing_speed >= 2.0:
                InfernalWrath = random.randint(1500,3000)
            elif typing_speed <= 2.0:
                InfernalWrath = random.randint(1250,2800)
            elif typing_speed <= 1.2:
                InfernalWrath = random.randint(1000,2350)
            else:
                InfernalWrath = random.randint(1150,2120)
            Carol_Attack += 500
            third_boss['Health'] -= InfernalWrath
            print(f"{YELLOW}You dealt {InfernalWrath} damage to Roufo. He now has {third_boss['Health']} hp left ")
            third_boss['Health'] -= Carol_Attack
            cleaver_final = random.randint(0,250)
            player_health -= third_boss['CleaverVeil']+cleaver_final
            Carol_Health -= third_boss['CleaverVeil']+cleaver_final
            
            print(f"{RED}Roufa dealt {third_boss['CleaverVeil']+cleaver_final} damage to you. You now have {player_health} hp left ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} damage to Roufa. Saad hp: {Carol_Health} Roufa hp: {third_boss['Health']} ")
        elif attack_boss == 'chaossurge':
            if typing_speed >= 2.0:
                        ChaosSurge = random.randint(1500,3000)
            elif typing_speed <= 2.0:
                        ChaosSurge = random.randint(1250,2900)
            elif typing_speed <= 1.2:
                        ChaosSurge = random.randint(1000,2600)
            else:
                ChaosSurge = random.randint(700,2450)
            
            Carol_Health += 250
            third_boss['Health'] -= ChaosSurge
            print(f"{YELLOW}You dealt {ChaosSurge} damage to Roufo. He now has {third_boss['Health']} hp left ")
            third_boss['Health'] -= Carol_Attack
            final_imperial = random.randint(0,250)
            player_health -= third_boss['ImperialDirge']+final_imperial
            Carol_Health -= third_boss['ImperialDirge']+final_imperial
            
            print(f"{RED}Roufa dealt {third_boss['CleaverVeil']+final_imperial} damage to you. You now have {player_health} hp left ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} damage to Roufa. Saad hp: {Carol_Health} Roufa hp: {third_boss['Health']} ")
            if third_boss['Health'] <= 0:
                print(f"So you wish to lost to the best...")
                break
            elif third_boss['Health'] > 0 and player_health < 0:
                print(f"You lost...")
                sys.exit()

    return InfernalWrath,ChaosSurge,player_health,player_power,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name

def dungeon_four(InfernalWrath,ChaosSurge,player_health,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name,fourth_boss):
    player_health += 15000
    print(f"Gri: We did it..Unbelievable ")
    print(f"Saad: Yeah since this is dungeon 4 we need to be extra careful ")
    print(f"Oh shoot I can hear footsteps ")
    VenomousDrakes =20000

    player_health += 1500
    while VenomousDrakes > 0:
        player_power = random.randint(275, 1325)
        ven_damage = random.randint(125, 825)
        attack_choice = input("Enter '1' to attack: ")
        if attack_choice == '1':
            VenomousDrakes -= player_power
            player_health -= ven_damage
            print(f"{YELLOW}You dealt {player_power} damage to VenmousDrake. He now has {VenomousDrakes} hp left! ")
            print(f"{RED}VenomousDrake dealt {ven_damage} damage to you. You now have {player_health} hp left! ")
            if player_health <= 0:
                print(f"You lost..")
                sys.exit()
            elif player_health >= 0 and VenomousDrakes <= 0:
                print(f"You won the battle! ")
                break
    print(f"{BLUE}Gri: That was a tough one..")
    time.sleep(2)
    print(f"Saad: Yeah..")
    time.sleep(2)
    print(f"Suddenly everything goes black and Gri hears a voice..")
    time.sleep(2)
    print(f"Long have we waited for a vessel to come..seek your destiny of life and death ")
    time.sleep(2)
    print(f"Gri: Did you hear that too? ")
    time.sleep(2)
    print(f"Saad: What, no?")
    time.sleep(2)
    print(f"Gri: Uh ok..Woah what's this big ass door")
    time.sleep(2)
    print(f"Gri: The hell is this??")
    time.sleep(2)
    print(f"You have entered the 'Volcano of EmberClif'")
    time.sleep(2)
    print(f"This area is-hey look at that THATS A FUCKING STAGE 2 ARTIFACT THERE GO FOR IT ")
    time.sleep(2)
    print(f"They obtain the 'HellBound Aegis' ")
    time.sleep(2)
    print(f"This is..a stage 2 artifact the hellbound aegis ")
    time.sleep(2)
    print(f"Saad: Should we apply its effect on ourselves? ")
    time.sleep(2)
    print(f"Gri: Definitely..")
    time.sleep(2)
    print(f"They touch it...A chill sweeps through the dungeon as they bear its overwhelming and overflowing energy..")

    player_health += 7500
    Carol_Health += 7000
    Carol_Attack += 500
    print(f"Your current hp is now {player_health} ")
    print(f"Saad's current hp is now {Carol_Health} ")
    print(f"{YELLOW}I feel so powerful..")
    print(f"I hear footsteps guard on ")
    Venomous_Lions = 5250

    while Venomous_Lions > 0:
        player_power += random.randint(375,1800)
        venlion_dmg = random.randint(400, 1750)
        attack_lions = input(f"{BLUE}Press '1' to attack: ")
        if attack_lions == '1':
            Venomous_Lions -= player_power
            player_health -= venlion_dmg
            print(f"{YELLOW}You dealt {player_power} damage to venomous lion.He now has {Venomous_Lions} hp left ")
            print(f"{RED}Venomous Lion dealt {venlion_dmg} damage to you. You now have {player_health} hp left ")
        if Venomous_Lions <= 0:
            print(f"{YELLOW}You defeated the enemy and obtained a reward! ")
            print(f"{RED}You just got Orb of Pure Light..")
            player_health += 12250
            print(f"Your hp has increased up to {player_health} ")
            break
        elif Venomous_Lions > 0 and player_health < 0:
            print(f"You lost the battle! ")
            sys.exit()
    print(f"{BLUE}Dam so strong..I wonder how strong the upcoming guy will be..")
    time.sleep(2)
    print(f"Gri: Don't got time to regret so let's do this..")
    time.sleep(2)
    print(f"Gri: Say saad I am still wondering about that so called oath ")
    time.sleep(2)
    print(f"Saad: Huh? Oh yeah I honnestly don't know why he didn't make any oath with us ")
    time.sleep(2)
    print(f"Looks like we found the boss room lets do this partner ")
    time.sleep(2)
    print(f"Flames dance across the walls of the obsidian chamber. The heat is suffocating as the Infernal Pyromancer descends from his fiery throne")
    while fourth_boss['Health'] > 0:
        start_time = time.time()
        attack_tyrant = input(f"{RED}Enter the name of your abilities to attack: ").lower()
        end_time = time.time()
        if attack_tyrant == 'infernalwrath':
            if typing_speed >= 2.0:
                InfernalWrath = random.randint(3750,5500)
            elif typing_speed <= 2.0:
                InfernalWrath = random.randint(3400,5000)
            elif typing_speed <= 1.5:
                InfernalWrath = random.randint(2750,4500)
            else:
                InfernalWrath = random.randint(2500,4250)
            Carol_Attack += 5000
            tyrant_random_one = random.randint(3000,8000)
            final_one_damage = fourth_boss['ShadowSlice']+tyrant_random_one
            fourth_boss['Health'] -= InfernalWrath
            print(f"{YELLOW}You dealt {ChaosSurge} damage to the flame tyrant. His hp is now {fourth_boss['Health']} hp ")
            fourth_boss['Health'] -= Carol_Attack
            player_health -= final_one_damage
            Carol_Health -= final_one_damage
            print(f"{RED}The flame tyrant dealt {final_one_damage} damage to you. Your hp is now {player_health} ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} damage to the flame tyrant. Saad hp: {Carol_Health} FlameTyrant hp: {fourth_boss['Health']}")
        elif attack_tyrant == 'chaossurge':
            if typing_speed >= 2.0:
                ChaosSurge = random.randint(2500,8200)
            elif typing_speed <= 2.0:
                ChaosSurge = random.randint(2450,7750)
            elif typing_speed <= 1.5:
                ChaosSurge = random.randint(2200,7450)
            else:
                ChaosSurge = random.randint(2150,7570)
            tyrant_random_two = random.randint(3500,6000)
            final_damage_two = fourth_boss['DivineWrath'] + tyrant_random_two
            fourth_boss['Health'] -= ChaosSurge
            print(f"{YELLOW}You dealt {ChaosSurge} damage to the flame tyrant. His hp is now {fourth_boss['Health']} hp ")
            fourth_boss['Health'] -= Carol_Attack
            player_health -= final_damage_two
            Carol_Health -= final_damage_two
            print(f"{RED}The flame tyrant dealt {final_damage_two} damage to you. Your hp is now {player_health} ")
            print(
                f"{YELLOW}Saad dealt {Carol_Attack} damage to the flame tyrant. Saad hp: {Carol_Health} FlameTyrant hp: {fourth_boss['Health']}")
        if fourth_boss['Health'] <= 0:
            print(f"You won this mightly battle and as a reward you obtained Lunar and Lance Amulet of Storm ")
            player_health += 12250
            player_power += 2500
        elif fourth_boss['Health'] > 0 and player_health <= 0:
            print(f"You lost..warriors ")
            sys.exit()
    return InfernalWrath,ChaosSurge,player_health,player_power,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name


def final_dungeon(InfernalWrath,ChaosSurge,player_health,player_power,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name):
    print(f"{BLUE}Saad: Gri, do you think we are the choosen ones? ")
    time.sleep(2)
    print(f"Gri: Choosen ones? For what? ")
    time.sleep(2)
    print(f"Saad: To win this battle! ")
    time.sleep(2)
    print(f"Gri: Maybe many more made it here and died? You can't be so sure ")
    time.sleep(2)
    print(f"Oh..well we've got company saad ")
    time.sleep(2)
    shadow_lords_hp = 25000
    while shadow_lords_hp > 0:
        shadow_lords_dmg = random.randint(575,1750)
        attack_lords = input("Press '1' to attack: ")
        player_power_addition = random.randint(100,150)
        if attack_lords == '1':
            final_power = player_power+player_power_addition
            shadow_lords_hp -= final_power
            player_health -= shadow_lords_dmg
            print(f"{YELLOW}You dealt {final_power} damage to shadow lord. He now has {shadow_lords_hp} hp left! ")
            print(f"{RED}Shadow lord dealt {shadow_lords_dmg} damage to you. You now have {player_health} hp left! ")
            if player_health <= 0:
                print(f"You lost..")
                sys.exit()
            elif player_health >= 0 and shadow_lords_hp <= 0:
                print(f"You won't get what you expect...humans! ")
                break
    print(f"Gri: Their durability is insane..he really lasted for some time depsite our crazy damage ")
    time.sleep(2)
    print(f"As Gri and Saad traverse the winding tunnels of the previous dungeon, they find themselves at the entrance of an ominous, ancient doorway")
    time.sleep(2)
    print(f"Saad: This is it Partner...")

    print(f"Your powers have increased ")
    Carol_Health += 125000
    player_health += 125000
    while final_boss['Health'] > 0:
        InfernalWrath_buff = random.randint(11250,15000)
        final_infernalwrath = InfernalWrath+InfernalWrath_buff
        reaper_damage_one = random.randint(15000,25250)
        reaper_damage_two = random.randint(13250,27550)
        start_time = time.time()
        attack_boss = input(f"{RED}Enter the name of your abilities to attack: ").lower()
        end_time = time.time()
        if attack_boss == 'infernalwrath':
            Carol_Attack += random.randint(5000,12500)
            final_boss['Health'] -= final_infernalwrath
            print(f"{YELLOW}You dealt {InfernalWrath} damage to the enemy. He now has {final_boss['Health']} hp left ")
            final_boss['Health'] -= Carol_Attack
            player_health -= reaper_damage_one
            Carol_Health -= reaper_damage_one
            print(f"{RED}AbyssalReaper dealt {reaper_damage_one} damage to you. You now have {player_health}hp left ")
            print(f"{YELLOW}Saad dealt {Carol_Attack} damage to AbyssalReaper. Saad's hp:{Carol_Health} , AbyssalReaper HP:{final_boss['Health']}")
        elif attack_boss == 'chaossurge':
            ChaosSurge_buff = random.randint(8000,17750)
            final_chaossurge = ChaosSurge+ChaosSurge_buff
            final_boss['Health'] -= ChaosSurge+ChaosSurge_buff
            print(f"{YELLOW}You dealt {ChaosSurge} damage to the enemy. He now has {final_boss['Health']} hp left ")
            final_boss['Health'] -= Carol_Attack
            player_health -= reaper_damage_two
            Carol_Health -= final_boss['SpectralScythe']
            print(f"{RED}AbyssalReaper dealt {reaper_damage_two} damage to you. You now have {player_health}hp left ")
            print(
                f"{YELLOW}Saad dealt {Carol_Attack} damage to AbyssalReaper. Saad's hp:{Carol_Health} , AbyssalReaper HP:{final_boss['Health']}")
        if final_boss['Health'] > 0 and player_health <= 0:
            print(f"You lost to the best...")
            sys.exit()
        elif final_boss['Health'] <= 0 and player_health > 0:
            print(f"You won the final battle")
            print(f"{CYAN}Hail as the king ")
            print(f"Gri and Saad's adventures will never end and they will keep conquering dungeons....")
player_intelligence,player_inventory, goblin_health, player_health, player_power, goblin_damage,first_boss,second_boss,healing_potion,third_boss,third_dung_eiser,fourth_boss,final_boss = main()
player_intelligence,player_inventory,MalevolentShrine,BeastChiller,typing_speed,damage_modifier,goblin_health,player_health,player_powers,goblin_damage = first_dungeon(player_intelligence, player_inventory, goblin_health, player_health, player_power, goblin_damage,first_boss)
player_intelligence, player_inventory, MalevolentShrine, BeastChiller, typing_speed, damage_modifier, player_health, player_power, healing_potion, Carol_Health, Carol_Attack, Carol_Special_name = second_dungeon(player_intelligence,player_inventory,MalevolentShrine,BeastChiller,typing_speed,damage_modifier,player_health,player_powers,second_boss,healing_potion)
InfernalWrath, ChaosSurge, player_health, player_power, player_inventory, Carol_Health, Carol_Attack, Carol_Special_name = third_dungeon(player_intelligence, player_inventory, MalevolentShrine, BeastChiller, typing_speed, damage_modifier, player_health, player_power,healing_potion,Carol_Health,Carol_Attack,Carol_Special_name,third_dung_eiser)
InfernalWrath, ChaosSurge, player_health, player_power, player_inventory, Carol_Health, Carol_Attack, Carol_Special_name = dungeon_four(InfernalWrath,ChaosSurge,player_health,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name,fourth_boss)
final_dungeon(InfernalWrath,ChaosSurge,player_health,player_power,player_inventory,Carol_Health,Carol_Attack,Carol_Special_name)
