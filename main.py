import font, time, loopGame, clear
"""
This's main file in project 
"""

font.coding() # to show Logo Roawd
time.sleep(5) # to wait 5s
clear.clearConsole() # to clean console
font.fristShow() # to show Logo Game

username = input("Enter your name: ")

print("Hello {:s} Chose your level !!\n\npress 1 for Easy Level\npress 2 for Middle Level\npress 3 for Hard Level\npress 4 to Exit".format(username))
level = input("Enter your level: ")
if not level.isdecimal(): # to check input if char or str show enter number and go to function NotFound
    loopGame.Game.notFound(username)
clear.clearConsole()
loopGame.Game.questions(int(level), username) # if number start to play