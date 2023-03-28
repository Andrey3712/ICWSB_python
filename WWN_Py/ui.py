import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nПрограмма 'Заметки'. Используйте функции:\n\n1 - вывод заметок\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выбор заметок по дате\n6 - выбор заметки по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Длина текста не менее {n} символов!\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbuy():
    print("Работа программы окончена")
