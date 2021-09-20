# importing random library
import random


# class used to display the map at the start of the game
class map:
    def __repr__(self):
        return """

         CONQUER THE UNCHARTED LANDS

YOU SPAWN HERE       ^^^^^^^
  .·´  Magic forest  |||||||
 (¸¸.·´  .·´                     
       .·´Old town  [+|+|+|]===== 
      (¸¸.·´  .·´         
            .·´ No man's land    x   x
           (¸¸.·´  .·´         -|-|-|-|-
                  
                 .·YOUR JOURNEY ENDS HERE (if you survive)  
                          """


# class to define main character's gear and abilities
class Main_character():
    def __init__(self, gear, magic):
        self.gear = gear
        self.magic = magic
        self.health = 150
        self.alive = True

    # function to allow main character to take damage in the first half of the game
    def damage(self):
        self.alive = True
        hit = random.randrange(10, 50)  # randomises damage player will take per enemy hit
        if hit > 1:
            print("The creature got a hit in on" + " " + player + " " + "for" + " " + str(hit) + "HP!")
            self.health -= hit
        if self.health < 1:
            self.alive = False
            print("You have died "
                  "RIP" + " " + player)
            exit()


# enemy class to specify enemy's name, their weapon and alive status
class Enemy(Main_character):
    def __init__(self, name, weapon):
        self.weapon = weapon
        self.health2 = 100
        self.alive = True
        self.name = name

    # function defining player's attack mechanism
    def attack(self):
        hit = random.randrange(10, 50)
        magic_hit = random.randrange(20, 60)
        gear = ["Flame sword", "Bow", "Magic spear"]
        magic = ["Charge", "Teleport", "Fury"]

        attack_sel = int(input("GEAR ATTACK(1)  or  MAGIC ATTACK(2)"))
        print('\n' * 2)  # prints 80 line breaks
        if attack_sel == 1:
            print(player + " " + "have attacked" + " " + self.name + " " + "with" + " " + random.choice(gear) + " "
                  + "for" + " " + str(hit) + "HP!")
            print('\n' * 1)  # prints 80 line breaks
            self.health2 -= hit

        elif attack_sel == 2:
            print(player + " " + "have attacked" + " " + self.name + " " + "with" + " " + random.choice(magic) + " "
                  + "for" + " " + str(magic_hit) + "HP!")
            print('\n' * 1)  # prints 80 line breaks
            self.health2 -= hit * 2

        if self.health2 < 1:
            foe.alive = False
            print("YOU SLAUGHTERED THE BEASTS")
            print('\n' * 2)  # prints 80 line breaks
            event1.event1()

    # this function specifies one of the three main events happening in the game
    # it is split into two different decision a player can make
    # this section is for the first decision selection
    def event1(self):
        decision = input("MORE ARE COMING!! RUN OR FIGHT TILL DEATH: ")
        decision = decision.lower()
        print('\n' * 80)  # prints 80 line breaks

        if decision == "fight till death":
            self.health2 = 100
            print("YOU WILL NOW FACE THE FINAL WAVE TO TAKE OVER THIS LAND!!")
            print('\n' * 2)
            print("***QUICK TIME EVENT IS ABOUT TO START***")
            print('\n' * 1)
            w = input("PRESS W TO HOLD OFF THE ENEMY: ")
            w = w.lower()  # lowers player input to avoid input errors
            if w == "w":
                print(player, " IS SLAUGHTERING THE CREATURES OF THIS LAND")
                print('\n' * 1)
            s = input("PRESS S TO HEAL: ")
            s = s.lower()
            if s == "s":
                print("HEALTH POTION HAVE BEEN USED")
                print('\n' * 1)
            d = input("PRESS D TO FINISH IT: ")
            d = d.lower()
            if d == "d":
                print(player, """JUST BEHEADED THE LAST CREATURE IN HIS WAY
                          THIS LAND IS NOW YOURS!!, MAGIC FOREST HAS BEEN CONQUERED!!""")
                print('\n' * 1)
                print("***NEW WEAPON ACQUIRED*** Warriors Axe [damage 2x]")
                location2.location2()  # calls location function to display player's progress



        # this section is for the second decision selection
        elif decision == "run":
            self.health2 = 100
            print("YOU HAVE BEEN OVERWHELMED BY THE ENEMY FORCE, TIME TO RE-GROUP AND PLAN AN ATTACK")
            print('\n' * 2)
            print("***QUICK TIME EVENT IS ABOUT TO START***")
            print('\n' * 1)
            w = input("PRESS W TO SNEAK ATTACK YOUR ENEMY: ")
            w = w.lower()
            if w == "w":
                print(player, " IS QUIETLY ELIMINATING THE CREATURES ONE BY ONE")
                print('\n' * 1)
            s = input("PRESS S TO PLANT MAGIC BOMBS: ")
            s = s.lower()
            if s == "s":
                print("MAGIC BOMBS HAVE BEEN PLACED AROUND THE CAMP")
                print('\n' * 1)
            d = input(player + " " + "YOU ARE ONE BUTTON AWAY FROM CLAIMING THIS LAND AS YOURS, PRESS D TO FINISH IT: ")
            d = d.lower()
            if d == "d":
                print("***EXPLOSIONS SOUNDS AND CREATURES BURNING***")
                print('\n' * 2)  # prints 80 line breaks
                print("THIS LAND IS NOW YOURS!!, MAGIC FOREST HAS BEEN CONQUERED!!")
                print('\n' * 1)
                print("***NEW WEAPON ACQUIRED*** Warriors Axe [damage 2x]")
                foe.alive = False
                location2.location2()

    # function to display player's current progress
    def location2(self):
        print('\n' * 2)  # prints 80 line breaks
        location = int(input("""Your journey path so far!, click 2 to cont.
                    
                                                    1 - Magic forest - CONQUERED
                                                    2 - Old town 
                                                    3 - No man's land
                                                    
                                                    : """))

        if location == 2:
            print('\n' * 2)  # prints 80 line breaks
            print("***YOU WILL NOW TRAVEL THE OUTER DIMENSION PORTAL***")
            print('\n' * 2)
            print("YOUR NEXT LOCATION TO CONQUER IS THE OLD TOWN [+|+|+|]=====")
            print('\n' * 3)  # prints 80 line breaks
            print(player + " " + "have encountered" + " " + foe.name + " " + "wielding" + " " + foe.weapon)
            event2.event2()

    # this function specifices event 2 out of 3
    # it is split into two different decision a player can make
    # this section is for the first decision selection
    def event2(self):
        decision = input("....FOLLOWED BY A LARGE PATROL NEAR THE BRIDGE! HIDE IN THE RIVER OR USE THE BOAT: ")
        decision = decision.lower()
        if decision == "hide in the river":
            print('\n' * 1)
            hide1 = input("PRESS F TO HOLD YOUR BREATH UNTIL THEY HAVE PASSED: ")
            hide1 = hide1.lower()
            if hide1 == "f":
                print('\n' * 1)
                print("NOW FOLLOWING THEIR TRAIL", player,
                      "IS STEALTHY HEADING TO THE OLD BAZAR WHERE THE CURRENT OLD TOWN LEADER IS GIVING HIS SPEECH,"
                      "PERFECT TIME FOR ASSASSINATION ")
            print('\n' * 2)  # prints 80 line breaks
            print("***1 HOUR LATER***")
            print('\n' * 2)  # prints 80 line breaks
            item = input(player + " " + "HAVE REACHED THE SHORE, PRESS F SEARCH AREA FOR ANYTHING USEFUL : ")
            item = item.lower()
            if item == "f":
                print(player, "FOUND A SMOKE BOMB AND FEW ARROWS")
                print('\n' * 1)
                assassination.assassination()



        # this section is for the second decision selection
        elif decision == "use the boat":
            print('\n' * 1)
            hide2 = input("PRESS E TO USE THE BOAT TO GET AWAY: ")
            hide2 = hide2.lower()
            if hide2 == "e":
                print("NOW USING THE BOAT UNDER THE CLOAK OF FOG", player,
                      "IS HEADING TO THE OLD BAZAR WHERE THE CURRENT OLD TOWN LEADER IS GIVING HIS SPEECH PERFECT TIME FOR ASSASSINATION")
            print('\n' * 2)  # prints 80 line breaks
            print("***30 MIN LATER***")
            print('\n' * 2)  # prints 80 line breaks
            item = input("PRESS F SEARCH AREA FOR ANYTHING USEFUL : ")
            item = item.lower()
            if item == "f":
                print(player, "FOUND A SMOKE BOMB AND FEW ARROWS")
                assassination.assassination()

    # this section allows the player to select out of two different assassination options
    # section section below is for assassination a
    def assassination(self):
        assasination = input(
            "UPON DISCOVERING THE AREA, PLAN YOUR ASSASSINATION: 'a'for bow shot or 'b' for smoke bomb kill: ")
        assasination = assasination.lower()
        if assasination == "a":
            print('\n' * 1)
            input(
                "YOU ARE NOW ONE SHOT AWAY FROM TAKING THE LEAD OF THE OLD TOWN, PRESS ENTER TO USE THE PRECISION KILL: ")
            print('\n' * 2)  # prints 80 line breaks
            print("***HEADSHOT***")
            print('\n' * 2)  # prints 80 line breaks
            print(player, "!! YOUR FOES ARE FLEEING FROM FEAR, OLD TOWN IS NOW YOURS!!!")
            print('\n' * 1)
            print("***NEW WEAPON ACQUIRED*** [Banished Soul Bow - extra stun damage]")
            location3.location3()



        # section section below is for assassination b
        elif assasination == "b":
            print('\n' * 1)
            smoke = input("PRESS U TO USE THE SMOKE BOMB: ")
            smoke = smoke.lower()
            if smoke == "u":
                print("***SMOKE BOMB GOING OFF***")
                print('\n' * 1)
                stab = input("NOW IS THE TIME, PRESS Q TO BURY YOUR DAGGER IN YOUR ENEMY: ")
                stab = stab.lower()
                print('\n' * 1)
                stab2 = input("...PRESS Q AGAIN TO ENSURE THE KILL VIA ANOTHER FATAL BLOW: ")
                stab2 = stab2.lower()

                if stab and stab2 == "q":
                    print('\n' * 1)
                    print(player, "!! SMOKE HAVE CLEARED AND YOUR FOES ARE FLEEING FROM FEAR, OLD TOWN IS NOW YOURS!!!")
                    print('\n' * 2)
                    print("***NEW WEAPON ACQUIRED*** [Banished Soul Bow - extra stun damage]")
                    location3.location3()

    # this function specifies event 3 out of 3
    # this event is split into sequential events with no player choice
    def event3(self):
        print("***", player, ",YOU ARE NOW IN NO MAN'S LAND WHICH HAVE NOT BEEN CONQUERED BEFORE BY ANY WARRIOR***")
        print('\n' * 2)  # prints 80 line breaks
        print("AS YOU ENTER THE UN-CONQUERED LANDS, YOU ARE EQUIPPED WITH: " + " " + main_last_level.gear +
              " and" + " " + main_last_level.magic)
        print('\n' * 2)  # prints 80 line breaks
        print("AS", player,
              "APPROACHES THE UNHOLY TEMPLE TO CONFRONT THE FINAL ENEMY IN HIS WAY, HE IS ATTACKED BY THE CARETAKER, THE RELIC MONSTER THE SERVANT OF GODS")
        print('\n' * 2)  # prints 80 line breaks
        dodge = input(player + " " + "IS CRITICALLY DAMAGED, PRESS T TO TAKE COVER IN THE TEMPLE: ")
        dodge = dodge.lower()
        if dodge == "t":
            print('\n' * 1)  # prints 80 line breaks
            heal = input("PRESS G TO USE SPARTAN'S FURY TO RESTORE HEALTH AND EXTRA DAMAGE POINTS: ")
            heal = heal.lower()
            if heal == "g":
                print('\n' * 1)  # prints 80 line breaks
                bomb = input("THE CARETAKER FOUND YOU!! PRESS B TO USE SMOKE BOMB IN YOUR ADVANTAGE: ")
                bomb = bomb.lower()
                if bomb == "b":
                    print('\n' * 1)  # prints 80 line breaks
                    attack = input("THE CARETAKER IS DISORIENTED, QUICKLY PRESS H FOR A POWERFUL MAGIC ATTACK: ")
                    attack = attack.lower()
                    if attack == "h":
                        print('\n' * 2)
                        print("***POWER INTENSIFIES***")
                        print('\n' * 2)
                        attack2 = input(
                            "THE CARETAKER IS ON BRINK OF DEATH, PRESS R TO DODGE HIS WRATH ATTACK AND DEAL FINAL BLOW: ")
                        attack2 = attack2.lower()
                        if attack2 == "r":
                            print('\n' * 2)  # prints 80 line breaks
                            print("***SUDDEN DODGE / / / /  ----------------> STRIKE***")
                            print('\n' * 2)  # prints 80 line breaks
                            print(player,
                                  "!!, HE IS MORE POWERFUL THAN EXPECTED, THE TEMPLE WILL BE SACRIFICED TO DEFEAT THE CARETAKER")
                            print('\n' * 1)  # prints 80 line breaks
                            final_strike = input(
                                "PRESS V TO USE YOUR BOW TO EXPLODE TEMPLE PILLARS WHICH WILL CRUSH THE ENEMY ENSURING OUR VICTORY!!: ")
                            final_strike = final_strike.lower()
                            if final_strike == "v":
                                print('\n' * 3)  # prints 80 line breaks
                                print("***MASSIVE EXPLOSION SOUNDS***")
                                print('\n' * 3)
                                print("IMPOSSIBLE HAVE HAPPENED", player, "HAVE CONQUERED NO MAN'S LAND")
                                print('\n' * 2)  # prints 80 line breaks
                                print("New weapon acquired [Blades of Chaos - damage 10x/fire damage +13]")
                                print('\n' * 3)
                                print(player + " " + "IS THE NEW RULER OF THESE UNCHARTED LANDS...TO BE CONTINUED")
                                exit()

    # function to display player's current progress
    def location3(self):
        print('\n' * 2)  # prints 2 line break
        location = int(input("""Your journey is almost over!, click 3 to cont.

                                                    1 - Magic forest - CONQUERED
                                                    2 - Old town - CONQUERED
                                                    3 - No man's land
                                                    
                                                    :"""))

        if location == 3:
            print('\n' * 2)  # prints 2 line break
            print("***You will now travel the outer dimension***")
            print("Your last location to conquer is the No Man's Land!")
            print('\n' * 3)  # prints 3 line break
            event3.event3()


# prints the map at the start of the game
print(map())

# allows player to input his name
player = str(input("\nEnter your hero's name: "))
player = player.upper()

# instantiation of all in game objects
gear = ["Flame sword", "Bow", "Magic spear"]
magic = ["Charge", "Teleport", "Fury"]
foe_names = ["Trolls", "Witches", "Werewolf's", "Vampires"]
foe_weapons = ["Great axes", "Rusty pipes", "Magic bombs", "Great bows"]
foe = Enemy(random.choice(foe_names), random.choice(foe_weapons))
main = Main_character(random.choice(gear), random.choice(magic))
main_last_level = Main_character("Banished Soul Bow", "Spartan's Fury")
event1 = Enemy(random.choice(foe_names), random.choice(foe_weapons))
event2 = Enemy(random.choice(foe_names), random.choice(foe_weapons))
event3 = Enemy(random.choice(foe_names), random.choice(foe_weapons))
location2 = Enemy(random.choice(foe_names), random.choice(foe_weapons))
location3 = Enemy(random.choice(foe_names), random.choice(foe_weapons))
assassination = Enemy(random.choice(foe_names), random.choice(foe_weapons))

# shows player's current equipment and magic skill per playthrough,
# current location on the map,
# and statemnt to randomise an enemy and a weapon type
print("You are equipped with" + " " + main.gear + " " + "and" + " " + main.magic)
print('\n' * 2)
print("""First location to conquer is the Magic Forest   ^^^^^^
                                                ||||||""")
print('\n' * 3)  # prints 3 line break
print(player + " " + "have encountered" + " " + foe.name + " " + "wielding" + " " + foe.weapon)

# while loop used for the fighting mechanism
# implements foe.attack function to allow the player to select his attack option,
# and main.damage to allow the player to take damage
while foe.alive == True:
    kill = input("\n press Enter to start an attack!")
    print('\n' * 2)  # prints 80 line breaks
    if kill == "":
        foe.attack()
        main.damage()
