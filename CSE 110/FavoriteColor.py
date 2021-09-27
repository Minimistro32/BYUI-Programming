'''
The Project was to return the user's favorite color back to them,
in order to get 100% I had to exceed the minimum specifications.
I ended up making this because it was enjoyable to create.
'''

class MinimumSpecifications:
    def __init__(self, favoriteColor = ''):
        self.favoriteColor = favoriteColor

    def printFavoriteColor(self):
        print(f"Your favorite color is \n{self.favoriteColor}")

    def setFavoriteColor(self):
        self.favoriteColor = input("Please type your favorite color: ")

class OverAchieving(MinimumSpecifications):
    #defaults to Violet because that's my favorite color
    #realColors default to the Rainbow because that is the Gag
    def __init__(self, favoriteColor= 'Violet', realColors = ['red','orange','yellow','green','blue','indigo','violet']):
        super().__init__(favoriteColor)
        self.realColorsArray = realColors

    def printFavoriteColor(self, name = ''):
        if name != '':
            name += ", "

        if self.__isValidColor():
            print(f"{name}Your favorite color '{self.favoriteColor}' actually does count as a color. Good pick! ")
        else:
            print(f"{name}'{self.favoriteColor}' isn't a real color 👀 !")

    def setFavoriteColor(self):
        self.favoriteColor = input("Please type your favorite color (🌈): ")

    def __isValidColor(self):
        #The 'ternary operator' is the best at over acheiving :D
        return False if len(self.realColorsArray) == 0 else self.favoriteColor.lower().strip() in map(lambda color: (color.lower().strip()), self.realColorsArray)

#array of SuperClass Objects
unnecessaryArray = [MinimumSpecifications(), OverAchieving()]

#polymorphism
userName = input("What is your name? ")
for homeworkObject in unnecessaryArray:
    print("\n")
    homeworkObject.setFavoriteColor()

    if type(homeworkObject) == OverAchieving:
        homeworkObject.printFavoriteColor(userName)
    else:
        homeworkObject.printFavoriteColor()
    
#any chance I can test out? JK, unless there really is a way to do that.
#  🥺
# 👉👈