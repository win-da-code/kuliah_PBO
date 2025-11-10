class Hero:
    __jumlah = 0

    def __init__(self, nama, health, attPower, armor):
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor

        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level
        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def gainEXP(self):
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP
        while self.__exp >= 100:
            self.__exp -= 100
            self.__level += 1
            print(f"{self.__name} level up")
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            self.__health = self.__healthMax

    def attack(self, musuh):
        self.gainEXP = 50

    @property
    def info(self):
        return f"{self.__name} level {self.__level}:\n" \
               f"\thealth = {self.__health}/{self.__healthMax}\n" \
               f"\tattack = {self.__attPower}\n" \
               f"\tarmor = {self.__armor}"


slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)
slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)
