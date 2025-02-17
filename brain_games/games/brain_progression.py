from random import randint

import brain_games.games.common_module as cm

STEP = 10
MIN_NAMBER = 5
MAX_NAMBER = 10

def brain_progression():
    name_user = cm.user_name()
    print('What number is missing in the progression?')
    for i in range(cm.NUMBER_ATTEMPTS):
        start = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        step = randint(1, STEP)
        number_elements = randint(MIN_NAMBER, MAX_NAMBER)
        hidden_value = randint(0, number_elements - 1)
        list_progression = arithmetic_progression(start, step, number_elements)
        cor_answer = list_progression[hidden_value]
        list_progression[hidden_value] = '..'
        expression = ' '.join(map(str, list_progression))
        cm.show_question(expression)
        user_answer = cm.enter_answer(True)
        if not cm.check_answer(user_answer, cor_answer, name_user):
            return
    cm.text_winner(name_user)


def arithmetic_progression(start, step, number_elements):
    return [start + step * i for i in range(number_elements)]

