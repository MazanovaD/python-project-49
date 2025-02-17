from math import gcd
from random import randint

import brain_games.games.common_module as cm


def brain_gcd():
    name_user = cm.user_name()
    print('Find the greatest common divisor of given numbers.')
    for i in range(cm.NUMBER_ATTEMPTS):
        value1 = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        value2 = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        expression = f'{value1} {value2}'
        cm.show_question(expression)
        user_answer = cm.enter_answer(True)
        cor_answer = gcd(value1, value2)
        if not cm.check_answer(user_answer, cor_answer, name_user):
            return
    cm.text_winner(name_user)
