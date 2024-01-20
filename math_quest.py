import math
import operator
import os
import random
import time

OPERATIONS = (operator.add, operator.sub, operator.mul, operator.truediv)
OP_STRINGS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "X",
    operator.truediv: "\u00F7",
}

COUNT_DOWN = 3
GAME_TIME = 30  # s

EASY = "EASY"
HARD = "HARD"
IMPOSSIBLE = "IMPOSSIBLE"

CORRECT_SCORE = 20
INCORRECT_SCORE = -10
HIGH_SCORE_FN = "high_score.txt"


class Players:
    evan = "EVAN"
    fred = "FRED"
    nolan = "NOLAN"
    mick = "MICK"
    melyssa = "MELYSSA"
    mom = "MOM"


DIFFICULTY_LUT = {
    Players.evan: EASY,
    Players.fred: EASY,
    Players.nolan: HARD,
    Players.mick: IMPOSSIBLE,
    Players.melyssa: IMPOSSIBLE,
    Players.mom: IMPOSSIBLE,
}
NUMBER_SIZE = {EASY: 10, HARD: 15, IMPOSSIBLE: 100}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def run_start_sequence():
    count = COUNT_DOWN
    while count > -1:
        clear_screen()
        print(f"Game starting in: {count}")
        time.sleep(1)
        count -= 1


def print_and_get_high_score():
    clear_screen()
    with open(HIGH_SCORE_FN, "r") as f:
        line = f.readline()
        high_score, name = line.split("\t")

    print(f"{name.upper()} has the High Score with {high_score} points!")
    time.sleep(3)
    return high_score


def save_high_score(score, name):
    with open(HIGH_SCORE_FN, "w") as f:
        f.write(f"{score}\t{name}")


def delete_high_score():
    try:
        os.remove(HIGH_SCORE_FN)
    except FileNotFoundError:
        return


def run_end_sequence(score, high_score, name):
    clear_screen()
    if score >= 200:
        print(f"okay Einstein, I get it, you're smarter than everyone else...")
    if score > high_score:
        print(f"You have a NEW HIGH SCORE!!!")
        delete_high_score()
        save_high_score(score, name)
        return
    if score <= 0:
        print(f"sorry, will have to work on your math skills...")
    elif score >= 100:
        print(f"holy crap, great job, you will soon beat that high score!")

    elif score >= 40:
        print(f"NOT bad, but could still use some work..")
    print(f"YOUR SCORE: {score}")
    print(f"High Score: {high_score}")


def get_number_size(name):
    upper_name = name.upper()
    if upper_name not in DIFFICULTY_LUT:
        difficulty = HARD
    else:
        difficulty = DIFFICULTY_LUT[upper_name]
    return NUMBER_SIZE[difficulty]


def get_random_operation():
    return random.choice(OPERATIONS)


def ask_for_name():
    clear_screen()
    return input("What is your first name?")


def ask_question(first_number, op, second_number):
    op_str = OP_STRINGS[op]
    clear_screen()
    while True:
        answer = input(f"What is {first_number:,} {op_str} {second_number:,}?")
        try:
            answer = int(answer)
        except ValueError:
            print("value must be a valid integer, try again!")
            continue
        return answer


def get_answer(first_number, op, second_number):
    return int(op(first_number, second_number))


def process_result_and_get_score(answer, correct_answer, score):
    if int(answer) == correct_answer:
        print(f"CORRECT")
        score += CORRECT_SCORE
    else:
        print(f"INCORRECT, the correct answer is: {correct_answer}")
        score += INCORRECT_SCORE
    score = int(score)
    print(f"SCORE: {score}")
    time.sleep(1)
    return score


def get_random_numer(number_size):
    rand = math.trunc(random.random() * number_size)
    if rand == 0:
        rand += 1
    return rand


def get_second_number(number_size):
    return get_random_numer(number_size)


def get_first_number(number_size, op, second_number):
    first = get_random_numer(number_size)
    if op == operator.truediv:
        return second_number * first
    else:
        return first


def main():
    try:
        high_score = int(print_and_get_high_score())
    except FileNotFoundError:
        high_score = 10
    name = ask_for_name()
    run_start_sequence()
    number_size = get_number_size(name)
    score = 0.0
    time_played = 0.0
    start_time = time.time()
    while time_played < GAME_TIME:
        second_number = get_second_number(number_size)
        op = get_random_operation()
        first_number = get_first_number(number_size, op, second_number)
        answer = ask_question(first_number, op, second_number)
        correct_answer = get_answer(first_number, op, second_number)
        # print(correct_answer, answer)
        score = process_result_and_get_score(answer, correct_answer, score)

        new_time = time.time()
        time_played = new_time - start_time

    run_end_sequence(score, high_score, name)


if __name__ == "__main__":
    while True:
        main()
        y_or_n = input("Do you want to play again (y or n?)")
        if y_or_n.upper() == "Y":
            continue
        break
