from random import randint
import prompt
import sys
sys.path.append('/home/malina/python-project-49/brain_games')
import cli

def brain_even():
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

        if person_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f'{person_answer} is wrong answer ;(. Correct answer was {answer}')
            exit()

    print(f'Congratulations, {cli.name}!')


brain_even()
