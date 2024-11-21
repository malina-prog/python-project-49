from random import randint
import prompt
import math
from brain_games.cli import welcome_user
from brain_games.scripts.games.game_test import test


def is_simple(n):
    if n == 1:
        return 'no'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        a = randint(1, 100)
        answer = is_simple(a)
        print(f'Question: {a}')
        person_answer = prompt.string('Your answer: ')
        count += test(answer, person_answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
