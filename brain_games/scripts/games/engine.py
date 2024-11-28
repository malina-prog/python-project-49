import prompt
from brain_games.cli import welcome_user


def welcome(game_quest):
    name = welcome_user()
    print(game_quest)
    return name


def print_question(question):
    print(question)


def comparison(answer, name):
    person_answer = prompt.string('Your answer: ')
    if person_answer == answer:
        print('Correct!')
        return 1
    else:
        print(f"{person_answer} is wrong answer ;(. ", end='')
        print(f'Correct answer was {answer}')
        print(f"Let's try again, {name}!")
        exit()


def congratulation(name):
    print(f'Congratulations, {name}!')
