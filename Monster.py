class Monster:
    def __init__(self, damage:int, health:int, player):
        self.damage = damage
        self.health = health
        self.player = player

    def attack(self):
        self.player.health -= self.damage
        print(f"The monster attacks the Player for {self.damage} damage!")
            
            if self.player.health <= 0:
                print("The player has been defeated.")
                self.player.game_over()


class Player:
    def __init__ (self, health:int, mana:int, damage, speed):
        self.health = health
        self.mana = mana
        self.speed = speed
        self.monster = None
        self.damage = damage

    def monster_attack(self):
        if self.monster:
            self.monster.attack()
        else:
            print("No monster to attack")

    def player_attack(self):
        if self.monster:
            self.monster.health -= self.damage
            print('The player attacks the monster for {self.damage} damage')
        
        if self.monster.health <= 0:
            print('The monster has been defeated.')
            self.monster.game_over()
        else:
            print('No monster to attack.')

        def game_over(self):
            print('Game Over....')

        monster1 = Monster(self.damage -5, 100, player)
        monster2 = Monster(10,100,player)
                  
                  
                  
                  
                  
                  
                  
                  
        

