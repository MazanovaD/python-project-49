from random import randint

import brain_games.games.common_module as cm


def brain_prime():
    name_user = cm.user_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(cm.NUMBER_ATTEMPTS):
        value = randint(cm.MIN_RANGE_VALUES, cm.MAX_RANGE_VALUES)
        cm.show_question(value)
        user_answer = cm.enter_answer()
        cor_answer = 'yes' if is_prime_number(value) else 'no'
        if not cm.check_answer(user_answer, cor_answer, name_user):
            return
    cm.text_winner(name_user)


def is_prime_number(value):
    for n in range(2, value // 2):
        if value % n == 0:
            return False
    return True
