list_1 = ['.com', '.ru', '.net']
list_2 = ['@']

def right_email(e_mail):
    right = False
    for i in list_1:
        if e_mail.endswith(i):
            for j in list_2:
                if j in e_mail:
                    right = True
    return right


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if right_email(recipient) and right_email(sender) is not True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.\n'
              'Введите правильный e-mail')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print('--------------')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print('--------------')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print('--------------')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
