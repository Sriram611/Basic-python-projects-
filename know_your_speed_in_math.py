import time
import random

OPERATORS = ['+', '-', '*']

MIN_OPERAND = 2
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10

def generateproblem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = (str(left) + ' ' + operator + ' ' + str(right))
    ans = eval(expr)
    return expr, ans

wrong = 0
input("press enter to start ")
print('- - - - - - - - - - - - -')

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, ans = generateproblem()
    while True:
        guess = input('problem #' + str(i+1) + ' : ' + expr + ' = ' )
        
        if guess == str(ans):
            break
        else:
            print("your answer was wrong please try again")
            wrong += 1

end_time =time.time()
total_time = end_time - start_time
total_time = round(total_time,2)

print('- - - - - - - - - - - - -')
print("good job, you have finished in ", total_time, "seconds")


