from random import randint
import math

from brain_games.consts import BRAIN_PRIME_INSTRUCTION 
from brain_games.engine import run_game


def is_simple(n):
    if n == 1:
        return 'no'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def get_num_and_prime_ans() -> tuple[int, str]:
    number = randint(1, 100)
    answer = is_simple(number)
    return number, answer

def run_prime_game():
    run_game(get_num_and_prime_ans, BRAIN_PRIME_INSTRUCTIONS)


def test_func():
    return get_num_and_prime_ans()
