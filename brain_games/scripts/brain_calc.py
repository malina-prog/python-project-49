from random import randint
import prompt
import sys
sys.path.append('/home/malina/python-project-49/brain_games')
import cli


def main():
    name = cli.welcome_user()
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
            if person_answer == answer:
                print('Correct!')
                count += 1
            else:
                print(f'{person_answer} is wrong answer ;(. Correct answer was {answer}')
                exit()
        elif c == 2:
            print(f'Question: {a} - {b}')
            answer = str(a - b)
            person_answer = prompt.string('Your answer: ')
            if person_answer == answer:
                print('Correct!')
                count += 1
            else:
                print(f'{person_answer} is wrong answer ;(. Correct answer was {answer}')
                exit()
        elif c == 3:
            print(f'Question: {a} * {b}')
            answer = str(a * b)
            person_answer = prompt.string('Your answer: ')
            if person_answer == answer:
                print('Correct!')
                count += 1
            else:
                print(f'{person_answer} is wrong answer ;(. Correct answer was {answer}')
                exit()
    
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
        