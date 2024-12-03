import random

from brain_games.consts import CALC_INSTRUCTION, MATH_SIGNS
from brain_games.engine import run_game


def get_expression_and_answer() -> tuple[str, str]:
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)
    expression = (f'{num1}{math_sign}{num2}')
    answer = str(eval(f'{num1}{math_sign}{num2}'))
    return expression, answer


def run_calc_game():
    run_game(get_expression_and_answer, CALC_INSTRUCTION)
