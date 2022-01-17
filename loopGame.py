import time
import random

class Game():
    global numberOne, numberTwo
    global continuation
    continuation = True
    numberOne, numberTwo = 0, 0
    time.sleep(2)

    def afterLoss():
        print("Do you want Play again!!\n\npress 1 for Easy Level\npress 2 for Middle Level\npress 3 for Hard Level\npress 4 to Exit")
        level = input("Enter your level: ")
        Game.questions(int(level))
    
    def notFound():
        print("Enter the number shown below!!\n\npress 1 for Easy Level\npress 2 for Middle Level\npress 3 for Hard Level\npress 4 to Exit")
        level = input("Enter your level: ")
        Game.questions(int(level))


    def questions(level):
        global points
        global continuation
        points = 0
        if int(level) == 1 : print("Easy Level")
        elif int(level) == 2 : print("Middle Level")
        elif int(level) == 3 : print("Hard Level")
        elif int(level) == 4 : print("Exit")
        else : print("Not Found!")

        while continuation :
            if int(level) == 1 :
                numberOne = random.randint(-9, 9)
                numberTwo = random.randint(-9, 9)
                sum = numberOne * numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(numberOne, numberTwo))
                if int(answer) == sum :
                    print("Correct")
                    points +=1
                else :
                    print("Incorrect")
                    print("your points is: ",points)
                    time.sleep(5)
                    print("Game Over")
                    Game.afterLoss()
                    break
            
            elif int(level) == 2 :
                numberOne = random.randint(-99, 99)
                numberTwo = random.randint(-9, 9)
                sum = numberOne * numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(numberOne, numberTwo))
                if int(answer) == sum :
                    print("Correct")
                    points +=1
                else :
                    print("Incorrect")
                    print("your points is: ",points)
                    time.sleep(5)
                    print("Game Over")
                    Game.afterLoss()
                    break
            
            elif int(level) == 3 :
                numberOne = random.randint(-99, 99)
                numberTwo = random.randint(-99, 99)
                sum = numberOne * numberTwo
                print("your points is: ",points)
                answer = input("{:d} x {:d} = ".format(numberOne, numberTwo))
                if int(answer) == sum :
                    print("Correct")
                    points +=1
                else :
                    print("Incorrect")
                    print("your points is: ",points)
                    time.sleep(5)
                    print("Game Over")
                    Game.afterLoss()
                    break
            
            elif int(level) == 4 :
                continuation = False
            
            else : 
                print("Erorr")
                time.sleep(5)
                Game.notFound()