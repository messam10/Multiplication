import font
"""
This's file for return Art Number by point
"""


class point:
    # This function to print one line of the number like this ░░██╗██╗
    def printNmber(first, second):
        print("{} {}".format(first.expandtabs(2), second))

    def secondNumber(res, *first):  # This function to print all of the number with second Num
        if res == 0:
            point.printNmber(first[0], font.zero1)
            point.printNmber(first[1], font.zero2)
            point.printNmber(first[2], font.zero3)
            point.printNmber(first[3], font.zero4)
            point.printNmber(first[4], font.zero5)
            point.printNmber(first[5], font.zero6)
        elif res == 1:
            point.printNmber(first[0], font.one1)
            point.printNmber(first[1], font.one2)
            point.printNmber(first[2], font.one3)
            point.printNmber(first[3], font.one4)
            point.printNmber(first[4], font.one5)
            point.printNmber(first[5], font.one6)
        elif res == 2:
            point.printNmber(first[0], font.two1)
            point.printNmber(first[1], font.two2)
            point.printNmber(first[2], font.two3)
            point.printNmber(first[3], font.two4)
            point.printNmber(first[4], font.two5)
            point.printNmber(first[5], font.two6)
        elif res == 3:
            point.printNmber(first[0], font.three1)
            point.printNmber(first[1], font.three2)
            point.printNmber(first[2], font.three3)
            point.printNmber(first[3], font.three4)
            point.printNmber(first[4], font.three5)
            point.printNmber(first[5], font.three6)
        elif res == 4:
            point.printNmber(first[0], font.four1)
            point.printNmber(first[1], font.four2)
            point.printNmber(first[2], font.four3)
            point.printNmber(first[3], font.four4)
            point.printNmber(first[4], font.four5)
            point.printNmber(first[5], font.four6)
        elif res == 5:
            point.printNmber(first[0], font.five1)
            point.printNmber(first[1], font.five2)
            point.printNmber(first[2], font.five3)
            point.printNmber(first[3], font.five4)
            point.printNmber(first[4], font.five5)
            point.printNmber(first[5], font.five6)
        elif res == 6:
            point.printNmber(first[0], font.six1)
            point.printNmber(first[1], font.six2)
            point.printNmber(first[2], font.six3)
            point.printNmber(first[3], font.six4)
            point.printNmber(first[4], font.six5)
            point.printNmber(first[5], font.six6)
        elif res == 7:
            point.printNmber(first[0], font.seven1)
            point.printNmber(first[1], font.seven2)
            point.printNmber(first[2], font.seven3)
            point.printNmber(first[3], font.seven4)
            point.printNmber(first[4], font.seven5)
            point.printNmber(first[5], font.seven6)
        elif res == 8:
            point.printNmber(first[0], font.eight1)
            point.printNmber(first[1], font.eight2)
            point.printNmber(first[2], font.eight3)
            point.printNmber(first[3], font.eight4)
            point.printNmber(first[4], font.eight5)
            point.printNmber(first[5], font.eight6)
        elif res == 9:
            point.printNmber(first[0], font.nine1)
            point.printNmber(first[1], font.nine2)
            point.printNmber(first[2], font.nine3)
            point.printNmber(first[3], font.nine4)
            point.printNmber(first[4], font.nine5)
            point.printNmber(first[5], font.nine6)

    def printPoint(num):  # to check first number
        if int(num) < 10 :num = num.zfill(2)  # to add 0 before number EX: 4 => 04
        
        res = [int(x) for x in str(num)]

        if res[0] == 0:
            point.secondNumber(res[1], font.zero1, font.zero2,
                               font.zero3, font.zero4, font.zero5, font.zero6)
        elif res[0] == 1:
            point.secondNumber(res[1], font.one1, font.one2, font.one3,
                               font.one4, font.one5, font.one6)
        elif res[0] == 2:
            point.secondNumber(res[1], font.two1, font.two2, font.two3,
                               font.two4, font.two5, font.two6)
        elif res[0] == 3:
            point.secondNumber(res[1], font.three1, font.three2,
                               font.three3, font.three4, font.three5, font.three6)
        elif res[0] == 4:
            point.secondNumber(res[1], font.four1, font.four2,
                               font.four3, font.four4, font.four5, font.four6)
        elif res[0] == 5:
            point.secondNumber(res[1], font.five1, font.five2,
                               font.five3, font.five4, font.five5, font.five6)
        elif res[0] == 6:
            point.secondNumber(res[1], font.six1, font.six2, font.six3,
                               font.six4, font.six5, font.six6)
        elif res[0] == 7:
            point.secondNumber(res[1], font.seven1, font.seven2,
                               font.seven3, font.seven4, font.seven5, font.seven6)
        elif res[0] == 8:
            point.secondNumber(res[1], font.eight1, font.eight2,
                               font.eight3, font.eight4, font.eight5, font.eight6)
        elif res[0] == 9:
            point.secondNumber(res[1], font.nine1, font.nine2,
                               font.nine3, font.nine4, font.nine5, font.nine6)
