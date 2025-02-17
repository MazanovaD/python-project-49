import prompt

NUMBER_ATTEMPTS = 3
MIN_RANGE_VALUES = 1
MAX_RANGE_VALUES = 100


def greet():
    print("Welcome to the Brain Games!")


def user_name():
    greet()
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    return name


def show_question(value):
    print(f'Question: {value}')


def check_answer(user_an, corr_an, name_user):
    if corr_an == user_an:
        print('Correct!')
        return True
    else:
        print(f"'{user_an}' is wrong answer ;(. Correct answer was '{corr_an}'."
              f"\nLet's try again, {name_user}!")
        return False


def enter_answer(enter_int=False):
    if enter_int:
        return prompt.integer("Your answer: ")
    else:
        return prompt.string("Your answer: ")


def text_winner(user):
    print(f'Congratulations, {user}!')