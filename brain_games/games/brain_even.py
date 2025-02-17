from random import randint

import brain_games.games.common_module as cm


def brain_even():
    name_user = cm.user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(cm.NUMBER_ATTEMPTS):
        value = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        cm.show_question(value)
        user_answer = cm.enter_answer()
        cor_answer = 'yes' if value % 2 == 0 else 'no'
        if not cm.check_answer(user_answer, cor_answer, name_user):
            return
    cm.text_winner(name_user)
