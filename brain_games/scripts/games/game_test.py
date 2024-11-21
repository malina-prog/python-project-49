

def test(answer, person_answer, name):
    if person_answer == answer:
        print('Correct!')
        return 1
    else:
        print(f"{person_answer} is wrong answer ;(. ", end='')
        print(f'Correct answer was {answer}')
        print(f"Let's try again, {name}!")
        exit()
