from random import randint
import prompt
import math
import sys
sys.path.append('/home/malina/python-project-49/brain_games')
import cli


def is_simple(n):
    if n == 1:
        return 'no'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


def main():
    name = cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        a = randint(1, 100)
        answer = is_simple(a)
        print(f'Question: {a}')
        person_answer = prompt.string('Your answer: ')
        if person_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"{person_answer} is wrong answer ;(. ", end='')
            print(f'Correct answer was {answer}')
            print(f"Let's try again, {name}")
            exit()
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
