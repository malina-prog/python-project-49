from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.games.game_test import test


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        a = randint(1, 100)
        print(f'Question: {a}')
        if a % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        person_answer = prompt.string('Your answer: ')
        count += test(answer, person_answer, name)

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
