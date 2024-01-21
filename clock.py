import math
import random

from prettytable import PrettyTable
import config


def convert_y_to_row(y):
    return config.CLOCK_SIZE - y


def draw_hour_ticks(clock):
    radius = config.CLOCK_RADIUS
    x_centre, y_centre = config.CLOCK_CENTRE

    for hour, angle_radians in zip(config.HOURS, config.CLOCK_RADIAN_ANGLES):
        delta_x = math.cos(angle_radians) * radius
        delta_y = math.sin(angle_radians) * radius

        x_pos = x_centre + delta_x
        y_pos = y_centre + delta_y
        col = int(round(x_pos))
        row = int(round(convert_y_to_row(y_pos)))
        clock[row][col] = hour


def get_random_hour_minute_tuple():
    hour = random.choice(config.HOURS)
    minute = random.choice(config.MINUTES)
    return hour, minute


def add_hand(clock, angle_radians, hand_radius, hand_letter):
    radius = int(round(hand_radius)) + 1
    x_centre, y_centre = config.CLOCK_CENTRE
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
    for _ in range(config.CLOCK_SIZE):
        clock_list.append([config.EMPTY_CHARACTER for _ in range(config.CLOCK_SIZE)])
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


def lookup_radians(index, minutes_index=0):
    minutes_fraction = config.MINUTES[minutes_index] / 60.0
    hour_fraction = minutes_fraction * 5.0 / 60.0
    hour_radians = hour_fraction * 2 * math.pi
    return config.CLOCK_RADIAN_ANGLES[index] - hour_radians


def clock(_):
    clock = get_blank_clock_list()
    draw_hour_ticks(clock)
    hour, minute = get_random_hour_minute_tuple()

    minute_index = get_time_index(minute, config.MINUTES)
    minute_radians = lookup_radians(minute_index)
    hour_index = get_time_index(hour, config.HOURS)
    hour_radians = lookup_radians(hour_index)

    add_hand(clock, minute_radians, config.MINUTE_RADIUS, config.MINUTE_CHARACTER)
    add_hand(clock, hour_radians, config.HOUR_RADIUS, config.HOUR_CHARACTER)

    print_clock(clock)
    answer = input(
        f"\nWhat time is it? Give to the nearest 5 minute increment,ie. 1:05\n"
    )
    correct_answer = f"{hour}:{minute:02}"
    return answer, correct_answer


if __name__ == "__main__":
    clock()
