import operator
import math
import random

OPERATIONS = (operator.add, operator.sub, operator.mul, operator.truediv)
OP_STRINGS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "X",
    operator.truediv: "\u00F7",
}


def ask_question(first_number, op, second_number):
    op_str = OP_STRINGS[op]
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


def get_random_numer(number_size):
    rand = math.trunc(random.random() * number_size)
    if rand == 0:
        rand += 1
    return rand


def get_random_operation():
    return random.choice(OPERATIONS)


def get_second_number(number_size):
    return get_random_numer(number_size)


def get_first_number(number_size, op, second_number):
    first = get_random_numer(number_size)
    if op == operator.truediv:
        return second_number * first
    else:
        return first


def arith(number_size):
    op = get_random_operation()
    second_number = get_second_number(number_size)
    first_number = get_first_number(number_size, op, second_number)
    answer = ask_question(first_number, op, second_number)
    correct_answer = get_actual_answer(first_number, op, second_number)
    return answer, correct_answer
