import random

from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def get_num_and_even_ans() -> tuple[int, str]:
    number = random.randint(1, 100)
    answer = 'yes' if is_even(number) else 'no'

    return number, answer


def run_even_game():
    run_game(get_num_and_even_ans, EVEN_INSTRUCTION)
