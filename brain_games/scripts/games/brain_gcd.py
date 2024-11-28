from random import randint
import math
from brain_games.scripts.games.engine import welcome, print_question, comparison, congratulation


def main():
    game_quest = "Find the greatest common divisor of given numbers."
    name = welcome(game_quest)
    count = 0
    while count != 3:
        a = randint(1, 100)
        b = randint(1, 100)
        print_question(f'Question: {a} {b}')
        answer = str(math.gcd(a, b))
        count += comparison(answer, name)
    congratulation(name)


if __name__ == '__main__':
    main()
