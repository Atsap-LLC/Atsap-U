def checkList(food):
    count = 0
    for item in food:
        count += 1
    x = "Your list contains {} food items!"
    print(x.format(count)) 