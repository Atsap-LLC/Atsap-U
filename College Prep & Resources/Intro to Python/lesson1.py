myFavoriteFoods = ["Macaroni & Cheese", "Hot Dogs", "Ravioli", "Hamburgers"]

def checkList(food):
    count = 0
    for item in food:
        count += 1
    print count

checkList(myFavoriteFoods)