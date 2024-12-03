import math
from random import randint

from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import run_game


def get_nums_and_gcd_ans() -> tuple[str, str]:
    num1, num2 = randint(1, 100), randint(1, 100)
    num_pair = (f'{num1} {num2}')
    answer = str(math.gcd(num1, num2))
    return num_pair, answer


def run_gcd_game():
    run_game(get_nums_and_gcd_ans, GCD_INSTRUCTION)
