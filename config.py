import math
import operator
import random
from enum import Enum, auto

import arith
import clock
import fraction

COUNT_DOWN = 3
GAME_TIME = 30

# SCORING
HIGH_SCORE_FN = "high_score.txt"
MAX_HIGH_SCORES = 10
CORRECT_SCORE = 20
INCORRECT_SCORE = -10

# SHOULD ADD TO 1.0
CLOCK_PERCENTAGE = 0.2
FRACTION_PERCENTAGE = 0.2
ARITH_PERCENTAGE = 0.6

QUESTION_TYPE = (
    (CLOCK_PERCENTAGE, clock.clock),
    (CLOCK_PERCENTAGE + FRACTION_PERCENTAGE, fraction.fraction),
    (CLOCK_PERCENTAGE + FRACTION_PERCENTAGE + ARITH_PERCENTAGE, arith.arith),
)


REPORTS = (
    (220, f"okay Einstein, I get it, you're smarter than everyone else..."),
    (180, f"What did you have for breakfast, Mathagetti???"),
    (160, f"Do you know Geoff Smart?"),
    (140, f"Sir Isaac Newton would be impressed!"),
    (120, f"SOLID SCORE"),
    (100, f"Holy crap, that was pretty quick."),
    (80, f"Good Job."),
    (60, f"baby steps"),
    (40, f"NOT bad, but could still use some work.."),
    (20, f"Yay, you got one!"),
    (0, f"Better luck next time..."),
    (-20, f"Slow down, you're just guessing."),
)
EASY = "EASY"
HARD = "HARD"
IMPOSSIBLE = "IMPOSSIBLE"


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

# ARITH
NUMBER_SIZE = {EASY: 10, HARD: 12, IMPOSSIBLE: 200}
OPERATIONS = (operator.add, operator.sub, operator.mul, operator.truediv)
OP_STRINGS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "X",
    operator.truediv: "\u00F7",
}

# FRACTIONS
DENOMINATORS = {
    EASY: (2, 4, 8),
    HARD: (3, 6, 9, 12, 15),
    IMPOSSIBLE: (5, 11, 33, 55, 78, 93),
}
NUMERATORS = list(range(1, 8))

# CLOCK
CLOCK_SIZE = 20
CLOCK_CENTRE = (CLOCK_SIZE / 2, CLOCK_SIZE / 2)
CLOCK_RADIUS = CLOCK_SIZE / 2 - 1
MINUTE_RADIUS = CLOCK_SIZE / 2 - 2
HOUR_RADIUS = CLOCK_SIZE / 2 - 5

CLOCK_RADIAN_ANGLES = [math.radians(a) for a in range(0, 360, 30)]
HOURS = (3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4)
MINUTES = (15, 10, 5, 0, 55, 50, 45, 40, 35, 30, 25, 20)

EMPTY_CHARACTER = " "
MINUTE_CHARACTER = "m"
HOUR_CHARACTER = "H"


class Keys(Enum):
    number_size = auto()
    denominators = auto()


def get_random_operation():
    return random.choice(OPERATIONS)


def get_operator_string(operator):
    return OP_STRINGS[operator]
