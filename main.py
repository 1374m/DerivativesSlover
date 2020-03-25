# imports for slove
import math

Number = float(input('enter the number : '))

#loop 
run = True

while run :
    # Q ---> Question
    Q = input(' does your number have any variable  ?(y, n)')

    if (Q is 'n'):
        answer = 0
        print('your answer is zero (0)')
        break

    elif (Q is 'y') :
        Variable = input('enter your variable : ')
        power = float(input('enter the power number for your number : '))

        if (power == 0):
            answer = 0
            print('your answer is zero(0)')
            break

        elif (power == 1):
            answer = Number
            print('your number is', Number)

        else :
            Number *= power
            power += -1
            print(Number, Variable,'**', power)
