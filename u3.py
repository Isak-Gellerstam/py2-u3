# Denna uppgift består av tre delar. I första delen ska du skapa en generell klass som heter Roboto. Sen ska du skapa klasser för BattleRobo och RepairRobot. De ska ärva från Robot.

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


class BattaleRobot(Robot):
    def laser(self):
        print(f"{self.name}: fired laser")

class RepairRobot(Robot):
    def repair(self):
        print(f"{self.name}: repairing")


br = BattaleRobot(85, "RB1")

br.walk()