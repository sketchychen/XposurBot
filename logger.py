# logger.py
import datetime


def audit(message):
    with open('audit.log', 'a+') as file:
        file.write(
            f'[{datetime.datetime.now()}]\n'
            f'{message}\n'
            f'------------------------\n'
        )
