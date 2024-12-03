from random import randint

from brain_games.consts import PROGRESSION_INSTRUCTION
from brain_games.engine import run_game


def get_progression_and_miss_num() -> tuple[str, str]:
    start = randint(1, 70)
    step = randint(2, 7)
    progression_list = []
    for i in range(10):
        progression_list.append(start)
        start += step
    unknown = randint(1, 8)
    answer = str(progression_list[unknown])
    progression_list[unknown] = '..'
    progression_str = str(' '.join(str(x) for x in progression_list))
    return progression_str, answer


def run_progression_game():
    run_game(get_progression_and_miss_num, PROGRESSION_INSTRUCTION)
