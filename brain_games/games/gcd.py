import math

from random import randint
from brain_games.consts import BRAIN_GCD_INSTRUCTION
from brain_games.engine import run_game


def get_nums_and_gcd_ans() -> tuple[str, str]:
        num1, num2 = randint(1, 100), randint(1, 100)
        num_pair = (f'{num1} {num2}')
        answer = str(math.gcd(a, b))
        return num_pair, answer


def run_gcd_game():
    run_game(get_nums_and_gcd_ans, BRAIN_GCD_INSTRUCTION)


def test_func():
    return get_nums_and_gcd_ans()
