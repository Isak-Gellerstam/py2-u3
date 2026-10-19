# Denna uppgift består av tre delar. I första delen ska du skapa en generell klass som heter Robot. 
# Sen ska du skapa klasser för BattleRobo och RepairRobot. De ska ärva från Robot.

# https://www.w3schools.com/python/python_inheritance.asp

# 1. Skapa huvudklassen "Robot".
# Ge klassen några instansvariabeler: 
# name, energy
# 2. Skapa BattleRobot
# 3. Skapa RepairRobot

import os
import subprocess

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


class Robot:
    def __init__(self,energy,name):
        self.energy = energy
        self.name = name

    def walk(self):
        print(f"{self.name}: walked one step")

    def status(self):
        print(f"{self.name}: energy: {self.energy}")


class BattaleRobot(Robot):

    def action_1(self):
        self.energy -= 5
        print(f"{self.name}: fired laser, {self.energy} energy ramaning")

class RepairRobot(Robot):

    def action_1(self,):
        self.energy -= 10
        print(f"{self.name}: repairing")


battale_bot = BattaleRobot(50, "battale_bot")

heal_bot = RepairRobot(100, "heal_bot")

battale_bot.status()
battale_bot.walk()
battale_bot.action_1()

heal_bot.action_1()
heal_bot.status()


# u5
squad = [battale_bot, heal_bot]

for bot in squad:
    bot.action_1()