class Player:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        self.__monster = None

    def attack(self):
        if self.__monster is not None:
            self.__monster.take_damage(self.__attack_power)

    def take_damage(self, damage):
        self.__health -= damage

    def is_alive(self):
        return self.__health > 0

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

    @property
    def attack_power(self):
        return self.__attack_power

    @property
    def monster(self):
        return self.__monster

    @monster.setter
    def monster(self, value):
        self.__monster = value

class Monster:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    def attack(self, player):
        player.take_damage(self.__attack_power)

    def take_damage(self, damage):
        self.__health -= damage

    def is_alive(self):
        return self.__health > 0

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

    @property
    def attack_power(self):
        return self.__attack_power