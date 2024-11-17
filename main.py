def is_correct(correctness):
    if correctness.find('@') > 0 and \
            (correctness[len(correctness) - 4: len(correctness)] == '.com' or
             correctness[len(correctness) - 4: len(correctness)] == '.net' or
             correctness[len(correctness) - 3: len(correctness)] == '.ru'):
        return True
    else:
        return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if is_correct(recipient) == False or is_correct(sender) == False:
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
    elif sender != "university.help@gmail.com":
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
