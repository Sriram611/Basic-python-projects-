import random

COLORS = ['R', 'B', 'G', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    generated_code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        generated_code.append(color) 

    return generated_code

def guess_code():
    while True:    
        guess_code = input("guess the code: ").upper().split(" ")

        if len(guess_code) != CODE_LENGTH:
            print(f"you must guess {CODE_LENGTH} colors.")
            continue

        for color in guess_code:
             if color not in COLORS:
                 print(f"invalid color: {color},try again.")
                 break
             
        else:
            break

    return guess_code

def check_code(guess_code,generated_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in generated_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] +=1

    for guess_color, generated_color in zip(guess_code, generated_code):
        if guess_color == generated_color:
            correct_pos += 1 
            color_count[guess_color] -= 1

    for guess_color, generated_color in zip(guess_code, generated_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos +=1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the color code.")
    print("The valid colors are ", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess,code)

        if correct_pos == CODE_LENGTH:
            print(f"you guessed the code in {attempts} tries!")  
            break

        print(f"correct position: {correct_pos} | incorrect position: {incorrect_pos}")

    else:
        print("you ran out of tries, the code was", *code)

if __name__ == "__main__":
    game()