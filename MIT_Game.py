import math
import random




class Dice():
    # assumes 6 sided

    def __init__(self, ap = False):
        self.sides = ["A","B","C","D","F","reroll"]
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

    def __init__(self, name, ap = False):
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

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa
'''
    def calculate_GPA(self):
        gpa_total = 0
        for course in self.get_courses():
            while True:
                current_roll = course.roll_dice()
                if current_roll != "reroll":
                    course.set_grade(current_roll)
                    break
            if course.ap:
                gpa_total += Game.GPA_dict[current_roll] + 1
            else:
                gpa_total += Game.GPA_dict[current_roll]
        self.gpa = gpa_total / len(self.get_courses())
'''

class Game():
    GPA_dict = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    def __init__(self, gpa):
        # GPA is required GPA to win
        self.players = []
        self.gpa = gpa

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
        user.gpa = gpa_total / len(user.get_courses())


def simulation(winningGPA = 4.0):
    for i in range(10000):
        

def main(winningGPA = 4.0):
    winningGPA = dsljf;ljksdljsdkljdslkds;aj;
    print("welcome to the MIT game!\n" +
          "the objective of the game is to get into MIT.\n" +
          "you need to get a GPA of " + winningGPA + " to win")
    while Tr