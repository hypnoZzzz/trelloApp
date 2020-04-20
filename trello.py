import sys
import requests
from createColumn import create_new_column
from read import read
from createTask import create_new_task
from move import check_for_emptiness, bloodhound

auth_params = {
    'key': '3834098155ea3749d3ea796c75171ea3',
    'token': '9697200f110adea0bf2e0a50ddc3193a494cfb4f091c5a21528ee68fceb12008'
}

# Адрес, на котором расположен API Trello, именно туда мы будем отправлять HTTP запросы.
base_url = "https://api.trello.com/1/{}"
board_id = 'yybrPe0r'

def callback():
    print('Что Вы хотите сделать?')
    print('1 - добавить задачу')
    print('2 - переместить задачу')
    print('3 - создать новую колонку')
    task_input = input('любой другой ввод - посмотреть список задач: ')

    if task_input == '1':
        create_new_task()

    elif task_input=='2':
        check_for_emptiness()
        bloodhound()
    elif task_input == '3':
        create_new_column()
    else:
        print('Список существующих задач: ')

callback()

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        read()
    elif sys.argv[1] == 'create':
        create(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'move':
        move(sys.argv[2], sys.argv[3])
