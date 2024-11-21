from random import randint
import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.games.game_test import test


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    while count != 3:
        a = randint(1, 100)
        b = randint(1, 100)
        c = randint(1, 3)
        if c == 1:
            print(f'Question: {a} + {b}')
            answer = str(a + b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer, name)
        elif c == 2:
            print(f'Question: {a} - {b}')
            answer = str(a - b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer, name)
        elif c == 3:
            print(f'Question: {a} * {b}')
            answer = str(a * b)
            person_answer = prompt.string('Your answer: ')
            count += test(answer, person_answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
