import math
import random
from decimal import *



class Dice():
    # assumes 6 sided

    def __init__(self, ap = False):
        self.sides = ["A","A","B","B","C","D"]

        if ap:
            random_number = random.randint(0,5)
            if random_number == 0 or random_number == 1:
                self.set_side6 = "B"
            elif random_number == 2 or random_number == 3:
                self.set_side6 = "C"
            elif random_number == 4 or random_number == 5:
                self.set_side6 = "D"


    def get_side6(self):
        return self.sides[5]

    def set_side6(self, new_side6):
        self.sides[5] = new_side6

    def roll(self):
        return self.sides[random.randint(0, 5)]

class Course:

    def __init__(self, name, ap=False):
        self.name = name
        self.ap = ap
        self.grade = "lmao"
        if self.ap:
            self.dice = Dice(True)
        else:
            self.dice = Dice()

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_AP(self):
        return self.ap

    def roll_dice(self):
        return self.dice.roll()


class Player():
    # courses is just an array of arrays with name & boolean that corresponds to ap
    def __init__(self, name, courses_info):
        self.name = name
        self.courses = []
        for course in courses_info:
            self.courses.append(Course(course[0], course[1]))
        self.gpa = 200000
        self.mit = False

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def get_acceptance(self):
        return self.mit

    def accepted(self):
        self.mit = True

    # for simulation only
    def return_calc_GPA(self):
        gpa_total = 0
        for course in self.get_courses():
            '''
            while True:
                current_roll = course.roll_dice()
                if current_roll != "reroll":
                    course.set_grade(current_roll)
                    break
            '''
            current_roll = course.roll_dice()
            course.set_grade(current_roll)
            if course.ap:
                gpa_total += Game.GPA_dict[current_roll] + 1
            else:
                gpa_total += Game.GPA_dict[current_roll]
        self.set_gpa(Decimal(gpa_total) / Decimal(len(self.get_courses())))
        return self.get_gpa()

class Game:
    GPA_dict = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    def __init__(self, gpa = 4.0):
        # GPA is required GPA to win
        self.players = []
        self.gpa = gpa

    def get_class_size(self):
        return len(self.players)

    def get_player(self, id):
        return self.players[id]

    def add_player(self, name, courses):
        self.players.append(Player(name, courses))

    def calculate_GPA(self, player_id):
        gpa_total = 0
        user = self.players[player_id]
        for course in user.get_courses():
            while True:
                current_roll = course.roll_dice()
                if current_roll != "reroll":
                    course.set_grade(current_roll)
                    break
            if course.ap:
                gpa_total += Game.GPA_dict[current_roll] + 1
            else:
                gpa_total += Game.GPA_dict[current_roll]
        user.gpa = Decimal(gpa_total) / Decimal(len(user.get_courses()))


    def mark_acceptance(self):
        for player in self.players:
            if player.get_gpa() >= self.gpa:
                player.accepted()

    def count_acceptance(self):
        acceptance_count = 0
        for player in self.players:
            if player.get_acceptance():
                acceptance_count += 1

        return acceptance_count

    def percent_acceptance(self):
        return Decimal(self.count_acceptance()) / Decimal(self.get_class_size())

    # for simulation
    def get_class_GPA(self):
        class_gpa_total = 0
        for player in self.players:
            class_gpa_total += player.return_calc_GPA()
        return Decimal(class_gpa_total) / Decimal(len(self.players))


def simulation(regs, aps, class_size=1000000, winningGPA=4.0):
    # totals of playerGPA based on their amount of reg classes and ap classes
    simul = Game(winningGPA)

    course_list = []
    for i in range(regs):
        course_list.append(["regclass" + str(i), False])
    for i in range(aps):
        course_list.append(["apclass" + str(i), True])
    for i in range(class_size):
        simul.add_player(str(regs) + "reg_" + str(aps) + "ap_testplayer" + str(i), course_list)
    class_gpa = simul.get_class_GPA()
    simul.mark_acceptance()
    print("average GPA of " + str(regs) + " regulars and " + str(aps) + " APs is " + str(class_gpa) +
          "\nthere was " + str(simul.count_acceptance()) + " accepted out of a class size of " +
          str(simul.get_class_size()) +
          "\nthe percent accepted was " + str(simul.percent_acceptance()))


'''
    reg5_ap1 = Game(winningGPA)
    reg4_ap2 = Game(winningGPA)
    reg3_ap3 = Game(winningGPA)
    reg2_ap4 = Game(winningGPA)
    reg1_ap5 = Game(winningGPA)
    reg0_ap6 = Game(winningGPA)
    # 6 regs 0 aps
    for i in range(1000000):
        reg6_ap0.add_player("6reg_0ap testplayer" + str(i),
                        [
                            ["regclass0", False], ["regclass1", False], ["regclass2", False],
                         ["regclass3", False], ["regclass4", False], ["regclass5", False]
                        ])
    class_gpa = reg6_ap0.get_class_GPA()
    reg6_ap0.mark_acceptance()
    print("average GPA of 6 regular and 0 APs is " + str(class_gpa) +
          "\nthere was " + str(reg6_ap0.count_acceptance()) + " accepted out of a class size of " +
          str(reg6_ap0.get_class_size()) +
          "\nthe percent accepted was " + str(reg6_ap0.percent_acceptance())) 
'''


def simulator():
    print("welcome to the simulator for our mit game! find michael's optimal strategy to get into mit!\n")
    min_gpa = 4.0
    regs = 6
    aps = 0
    class_size = 1000000
    while True:
        min_gpa = Decimal(input("\npick a minimum gpa.\n? "))
        regs = int(input("\nhow many regular classes?\n? "))
        aps = int(input("\nhow many ap classes?\n? "))
        class_size = int(input("\nhow big should the sample size be?\n? "))
        print("\ncalculating odds...\n\n")
        simulation(regs, aps, class_size, min_gpa)

simulator()


'''
def main(winningGPA = 4.0):
    winningGPA = dsljf;ljksdljsdkljdslkds;aj;
    print("welcome to the MIT game!\n" +
          "the objective of the game is to get into MIT.\n" +
          "you need to get a GPA of " + winningGPA + " to win")
    while Tr


'''