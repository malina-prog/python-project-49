import math
from random import randint

from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_simple(number):
    if number == 1:
        return 'no'
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_num_and_prime_ans() -> tuple[int, str]:
    number = randint(1, 100)
    answer = is_simple(number)
    return number, answer


def run_prime_game():
    run_game(get_num_and_prime_ans, PRIME_INSTRUCTION)
