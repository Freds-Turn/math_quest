import os
import random
import time

import arith
import clock

CORRECT_SCORE = 20
INCORRECT_SCORE = -10

CLOCK_PERCENTAGE = 0.5

GAME_TIME = 30  # s


def correct(answer, correct_answer):
    if str(answer) == str(correct_answer):
        return True
    else:
        return False


def print_report(answer, correct_answer):
    if str(answer) == str(correct_answer):
        print("CORRECT")
    else:
        print(f"ERRRRR, WRONG... the correct answer was: {correct_answer}")


def update_score(correct_answer, score):
    """returns new score, based on correct answer boolean"""
    if correct_answer:
        score += CORRECT_SCORE
    else:
        score -= INCORRECT_SCORE
    return score


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def play_game_loop(number_size):
    """number size represents the max size of the base integers being used"""

    score = 0
    time_played = 0.0
    start_time = time.time()
    while time_played < GAME_TIME:
        clear_screen()
        if random.random() < CLOCK_PERCENTAGE:
            answer, correct_answer = clock.clock()
        else:
            answer, correct_answer = arith.arith(number_size)

        print_report(answer, correct_answer)

        check_mark = correct(answer, correct_answer)
        score = update_score(check_mark, score)
        new_time = time.time()
        time_played = new_time - start_time
        time.sleep(1)
    return score
