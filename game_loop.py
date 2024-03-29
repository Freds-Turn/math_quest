import os
import random
import time

from config import (
    CORRECT_SCORE,
    INCORRECT_SCORE,
    QUESTION_TYPE,
    GAME_TIME,
)


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


def update_score(check_mark_boolean, score):
    """returns new score, based on correct answer boolean"""
    if check_mark_boolean:
        score += CORRECT_SCORE
    else:
        score += INCORRECT_SCORE
    return score


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def play_game_loop(play_data):
    """number size represents the max size of the base integers being used"""

    score = 0
    time_played = 0.0
    start_time = time.time()
    while time_played < GAME_TIME:
        clear_screen()
        for percent, game_type_func in QUESTION_TYPE:
            if random.random() < percent:
                answer, correct_answer = game_type_func(play_data)
                break

        print_report(answer, correct_answer)

        check_mark = correct(answer, correct_answer)
        score = update_score(check_mark, score)
        new_time = time.time()
        time_played = new_time - start_time
        time.sleep(1)
    return score
