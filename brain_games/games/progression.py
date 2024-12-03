from random import randint
from brain_games.consts import BRAIN_EVEN_INSTRUCTION
from brain_games.engine import run_game


def get_progression():
    start = randint(1, 70)
    step = randint(1, 5)
    progression_list = []
    for i in range(10):
        progression_list.append(start)
        start += step
    unknown = randint(1, 8)
    answer = str(progression_list[unknown])
    progression_list[unknown] = '..'
    progression_str = str(' '.join(str(x) for x in progression_list))
    return progression_str, answer


def get_progression_and_answer() -> tuple[str, str]:
    progression, answer = get_progression()


def run_progression_game():
    run_game(get_progression_and_answer, BRAIN_PROGRESSION_INSTRUCTION)


def test_func():
    return get_progression_and_answer()
