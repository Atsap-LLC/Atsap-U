import mymodule

class Food:
    def __init__(self, name):
        self.name = name

myFoodList = []

count = 0
while count < 3:
    print("Enter the name of your favorite food")
    name = raw_input()
    x = Food(name)
    myFoodList.append(x)
    count += 1

mymodule.checkList(myFoodList)