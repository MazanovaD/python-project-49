from random import choice, randint

import brain_games.games.common_module as cm


def brain_calc():
    name_user = cm.user_name()
    list_choice = ['-', '+', '*']
    print('What is the result of the expression?')
    for i in range(cm.NUMBER_ATTEMPTS):
        value1 = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        value2 = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        value3 = choice(list_choice)
        expression = f'{value1} {value3} {value2}'
        cm.show_question(expression)
        user_answer = cm.enter_answer(True)
        cor_answer = eval(expression)
        if not cm.check_answer(user_answer, cor_answer, name_user):
            return
    cm.text_winner(name_user)
