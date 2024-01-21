import math
import operator
import random

import config


def ask_question(first_number, op_str, second_number):
    while True:
        answer = input(f"What is {first_number:,} {op_str} {second_number:,}?")
        try:
            answer = int(answer)
        except ValueError:
            print("value must be a valid integer, try again!")
            continue
        return answer


def get_actual_answer(first_number, op, second_number):
    return int(op(first_number, second_number))


def get_random_number(number_size):
    rand = math.trunc(random.random() * number_size)
    if rand == 0:
        rand += 1
    return rand


def get_random_operation():
    return random.choice(config.OPERATIONS)


def get_operator_string(operator):
    return config.OP_STRINGS[operator]


def get_second_number(number_size):
    return get_random_number(number_size)


def get_first_number(number_size, op, second_number):
    first = get_random_number(number_size)
    if op == operator.truediv:
        return second_number * first
    else:
        return first


def arith(play_data):
    number_size = play_data[config.Keys.number_size]
    op = config.get_random_operation()
    op_str = config.get_operator_string(op)
    second_number = get_second_number(number_size)
    first_number = get_first_number(number_size, op, second_number)
    answer = ask_question(first_number, op_str, second_number)
    correct_answer = get_actual_answer(first_number, op, second_number)
    return answer, correct_answer
