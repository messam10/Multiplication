import time, random, font, clear, point
"""
This's Game Engine to play and replay
"""
class Game():
    global __numberOne, __numberTwo # to get number from random and Multiplication
    __numberOne, __numberTwo = 0, 0

    def afterLoss(username): # This's function to show user after loss the Game
        print("Hi ", username)
        print("Do you want Play again!!\n\npress 1 for Easy Level\npress 2 for Middle Level\npress 3 for Hard Level\npress 4 to Exit")
        level = input("Enter your level: ")
        if not level.isdecimal():
            Game.notFound(username)
        clear.clearConsole()
        Game.questions(int(level), username)
    
    def notFound(username): # This's function to show user Wrong chose
        clear.clearConsole()
        print("Hi ", username)
        print("Enter the number shown below!!\n\npress 1 for Easy Level\npress 2 for Middle Level\npress 3 for Hard Level\npress 4 to Exit")
        level = input("Enter your level: ")
        if not level.isdecimal():
            Game.notFound(username)
        clear.clearConsole()
        Game.questions(int(level), username)

    def questions(level, username): # This's function to Start Game for all levels
        global points
        points = 0
        if level == 1 : print("Easy Level") # to show his\her chose
        elif level == 2 : print("Middle Level")
        elif level == 3 : print("Hard Level")
        elif level == 4 : print("Exit")
        else : print("Not Found!")

        while True :
            if level == 1 : # if Easy level
                __numberOne = random.randint(-9, 9)
                __numberTwo = random.randint(-9, 9)
                sum = __numberOne * __numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if answer.isalpha():
                    print("Enter Number ")
                    answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if int(answer) == sum :
                    font.correct()
                    points +=1
                else :
                    font.incorrect()
                    time.sleep(5)
                    clear.clearConsole()
                    font.point()
                    point.point.printPoint(str(points))
                    font.gameOver()
                    Game.afterLoss(username)
                    break
            
            elif level == 2 : # if Middle level
                __numberOne = random.randint(-99, 99)
                __numberTwo = random.randint(-9, 9)
                sum = __numberOne * __numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if answer.isalpha():
                    print("Enter Number ")
                    answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if int(answer) == sum :
                    font.correct()
                    points +=1
                else :
                    font.incorrect()
                    time.sleep(5)
                    clear.clearConsole()
                    font.point()
                    point.point.printPoint(str(points))
                    font.gameOver()
                    Game.afterLoss(username)
                    break
            
            elif level == 3 : # if Hard level
                __numberOne = random.randint(-99, 99)
                __numberTwo = random.randint(-99, 99)
                sum = __numberOne * __numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if answer.isalpha():
                    print("Enter Number ")
                    answer = input("{:d} x {:d} = ".format(__numberOne, __numberTwo))
                if int(answer) == sum :
                    font.correct()
                    points +=1
                else :
                    font.incorrect()
                    time.sleep(5)
                    clear.clearConsole()
                    font.point()
                    point.point.printPoint(str(points))
                    font.gameOver()
                    Game.afterLoss(username)
                    break
            
            elif level == 4 : # if want to Exit
                exit()
            
            else : # if Wrong chose
                font.error()
                time.sleep(5)
                clear.clearConsole()
                Game.notFound(username)