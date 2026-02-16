# class parent1:
#     pass
# class parent2:
#     pass
# class chils(parent1, parent2):
#     pass

class Father:
    def driving(self):
        print("Father has the skills to drive")
class Mother:
    def cooking(self):
        print("Mother has the skills to cook")
class Child(Father, Mother):
    def bothskills(self):
        print("Child has both skills of driving and cooking")

a = Child()
a.driving()
a.cooking()
a.bothskills()