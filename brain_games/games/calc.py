import random

from brain_games.consts import BRAIN_CALC_INSTRUCTION, MATH_SIGNS
from brain_games.engine import run_game


def get_expression_and_answer() -> tuple[str, int]:
    num1, num2 = random.randint(1,100), random.randint(1,100)
    math_sign = random.choice(MATH_SIGNS)
    expression = (f'{num1}{math_sign}{num2}')
    answer = eval(f'{num1}{math_sign}{num2}')
    return expression,answer

def run_calc_game():
    run_game(get_expression_and_answer, BRAIN_CALC_INSTRUCTION)


def test_func():
    return get_expression_and_answer()