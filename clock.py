import math
import random

from prettytable import PrettyTable

CLOCK_SIZE = 20
CLOCK_CENTRE = (CLOCK_SIZE / 2, CLOCK_SIZE / 2)
CLOCK_RADIUS = CLOCK_SIZE / 2 - 1
MINUTE_RADIUS = CLOCK_SIZE / 2 - 2
HOUR_RADIUS = CLOCK_SIZE / 2 - 5

EMPTY_CHARACTER = " "
MINUTE_CHARACTER = "m"
HOUR_CHARACTER = "H"

CLOCK_RADIAN_ANGLES = [math.radians(a) for a in range(0, 360, 30)]
HOURS = (3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5, 4)
MINUTES = (15, 10, 5, 0, 55, 50, 45, 40, 35, 30, 25, 20)


def convert_y_to_row(y):
    return CLOCK_SIZE - y


def draw_hour_ticks(clock):
    radius = CLOCK_RADIUS
    x_centre, y_centre = CLOCK_CENTRE

    for hour, angle_radians in zip(HOURS, CLOCK_RADIAN_ANGLES):
        delta_x = math.cos(angle_radians) * radius
        delta_y = math.sin(angle_radians) * radius

        x_pos = x_centre + delta_x
        y_pos = y_centre + delta_y
        col = int(round(x_pos))
        row = int(round(convert_y_to_row(y_pos)))
        clock[row][col] = hour


def get_random_hour_minute_tuple():
    hour = random.choice(HOURS)
    minute = random.choice(MINUTES)
    return hour, minute


def add_hand(clock, angle_radians, hand_radius, hand_letter):
    radius = int(round(hand_radius)) + 1
    x_centre, y_centre = CLOCK_CENTRE
    for r in range(radius):
        delta_x = math.cos(angle_radians) * r
        delta_y = math.sin(angle_radians) * r

        x_pos = x_centre + delta_x
        y_pos = y_centre + delta_y
        col = int(round(x_pos))
        row = int(round(convert_y_to_row(y_pos)))
        clock[row][col] = hand_letter


def get_blank_clock_list():
    clock_list = []
    for _ in range(CLOCK_SIZE):
        clock_list.append([EMPTY_CHARACTER for _ in range(CLOCK_SIZE)])
    return clock_list


def print_clock(clock_list):
    table = PrettyTable()
    table.border = False
    table.header = False
    table.padding_width = 1
    for row in clock_list:
        table.add_row(row)
        # for cell in row:
        #     print(cell)
    print(table)


def get_time_index(time, time_list):
    return time_list.index(time)


def lookup_radians(index):
    return CLOCK_RADIAN_ANGLES[index]


def clock():
    clock = get_blank_clock_list()
    draw_hour_ticks(clock)
    hour, minute = get_random_hour_minute_tuple()

    hour_index = get_time_index(hour, HOURS)
    minute_index = get_time_index(minute, MINUTES)
    hour_radians = lookup_radians(hour_index)
    minute_radians = lookup_radians(minute_index)
    add_hand(clock, minute_radians, MINUTE_RADIUS, MINUTE_CHARACTER)
    add_hand(clock, hour_radians, HOUR_RADIUS, HOUR_CHARACTER)

    print_clock(clock)
    answer = input(f"What time does the clock tell to the closest 5 minute ie.  1:05 ")
    correct_answer = f"{hour}:{minute:02}"
    return answer, correct_answer


if __name__ == "__main__":
    clock()
