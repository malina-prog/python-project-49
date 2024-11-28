from random import randint
import math
from brain_games.scripts.games.engine import welcome, print_question
from brain_games.scripts.games.engine import comparison, congratulation


def is_simple(n):
    if n == 1:
        return 'no'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def main():
    game_quest = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    name = welcome(game_quest)
    count = 0
    while count != 3:
        a = randint(1, 100)
        answer = is_simple(a)
        print_question(f'Question: {a}')
        count += comparison(answer, name)
    congratulation(name)


if __name__ == '__main__':
    main()
