import random
from fractions import Fraction

from config import Keys, NUMERATORS




def choose_random(values):
    return random.choice(values)


def get_random_fraction(denominators):
    numerator = choose_random(NUMERATORS)
    denom = choose_random(denominators)
    return Fraction(numerator, denom)


def ask_question(fraction1, fraction2):
    answer = input(
        f"What is "
        f"{fraction1.numerator}/{fraction1.denominator}"
        f" + "
        f"{fraction2.numerator}/{fraction2.denominator}?"
    )
    return answer


def get_correct_answer(fraction1, fraction2):
    correct_answer = fraction1 + fraction2
    return f"{correct_answer.numerator}/{correct_answer.denominator}"


def fraction(play_data):
    denominators = play_data[Keys.denominators]
    fraction1 = get_random_fraction(denominators)
    fraction2 = get_random_fraction(denominators)
    answer = ask_question(fraction1, fraction2)
    correct_answer = get_correct_answer(fraction1, fraction2)
    return answer, correct_answer
