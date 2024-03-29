import os
import time

from prettytable import PrettyTable

import game_loop
import config
from game_loop import clear_screen


def run_count_down_to_start():
    """counts down to the start of the game"""
    count = config.COUNT_DOWN
    while count > -1:
        clear_screen()
        print(f"Game starting in: {count}")
        time.sleep(1)
        count -= 1


def get_high_scores_from_file():
    """returns a list of high score tuples (score, name)"""
    high_scores = []
    with open(config.HIGH_SCORE_FN, "r") as f:
        lines = f.readlines()
        for line in lines:
            high_score, name = line.split("\t")
            high_scores.append((int(high_score), name.strip()))
    return high_scores


def get_place_on_high_score_list(high_scores, score):
    """returns the place, need to run this before scores are updated"""
    for index, (high_score, _) in enumerate(high_scores):
        if score > high_score:
            return index + 1
    if len(high_scores) < config.MAX_HIGH_SCORES:
        return len(high_scores) + 1
    return False


def update_high_scores_list(high_scores, score, name):
    """returns the place or False if they didn't make the list"""
    high_score_bool = False
    for index, (high_score, _) in enumerate(high_scores):
        if score > high_score:
            high_scores.insert(index, (score, name))
            high_score_bool = True
            break
    if len(high_scores) < config.MAX_HIGH_SCORES and not high_score_bool:
        high_scores.append((score, name))
    if len(high_scores) > config.MAX_HIGH_SCORES:
        high_scores.pop()


def print_high_scores(high_scores):
    table = PrettyTable()
    table.field_names = ["Place", "Name", "Score"]
    place = 1
    for high_score, name in high_scores:
        table.add_row([place, name, high_score])
        place += 1
    print(table)


def delete_high_score_file():
    try:
        os.remove(config.HIGH_SCORE_FN)
    except FileNotFoundError:
        return


def save_high_scores_list_to_file(high_scores):
    """
    save high scores list to file
    [(score, name), (score2, name2),...]
    """
    with open(config.HIGH_SCORE_FN, "w") as f:
        for index, (score, name) in enumerate(high_scores):
            f.write(f"{score}\t{name}")
            if index + 1 == len(high_scores):
                break
            f.write("\n")


def ordinal(n):
    if 10 <= n % 100 < 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return str(n) + suffix


def congratulate_high_score(high_score_place):
    """returns None"""
    if high_score_place:
        print(f"CONGRATULATIONS, you have a NEW HIGH SCORE!!!")
        if high_score_place == 0:
            print(f"You are the BEST of the BEST!!!")
        else:
            print(f"You are in {ordinal(high_score_place)} place.")


def give_report_card(score):
    """returns None"""
    for report_score, report in config.REPORTS:
        if score >= report_score:
            print(report)
            break


def get_difficulty(name):
    upper_name = name.upper()
    if upper_name not in config.DIFFICULTY_LUT:
        return config.HARD
    else:
        return config.DIFFICULTY_LUT[upper_name]


def get_number_size(difficulty):
    return config.NUMBER_SIZE[difficulty]


def get_denominators(difficulty):
    return config.DENOMINATORS[difficulty]


def ask_for_players_name():
    return input("What is your first name?")


def main():
    """main entry to game"""
    high_scores = get_high_scores_from_file()

    clear_screen()
    print_high_scores(high_scores)
    time.sleep(3)

    clear_screen()
    name = ask_for_players_name()
    difficulty = get_difficulty(name)
    number_size = get_number_size(difficulty)
    denominators = get_denominators(difficulty)
    play_data = {
        config.Keys.number_size: number_size,
        config.Keys.denominators: denominators,
    }
    run_count_down_to_start()
    score = game_loop.play_game_loop(play_data)
    high_score_place = get_place_on_high_score_list(high_scores, score)
    update_high_scores_list(high_scores, score, name)
    delete_high_score_file()
    save_high_scores_list_to_file(high_scores)

    clear_screen()
    give_report_card(score)
    time.sleep(1)
    congratulate_high_score(high_score_place)
    time.sleep(3)

    clear_screen()
    print_high_scores(high_scores)


def play_again():
    y_or_n = input("\nDo you want to play again (y or n?)")
    if y_or_n.upper() == "Y":
        return True
    print("Goodbye")


if __name__ == "__main__":
    while True:
        main()
        if not play_again():
            break
