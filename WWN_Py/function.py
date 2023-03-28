import file_operation
import Note
import ui

number = 7


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    array = file_operation.read_file()
    logic = True
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
        print('\nДата введена не корректно или заметок на эту дату нет!\nПовторите ввод, используя функцию ввода')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
            else:
                logic == True

    file_operation.write_file(array, 'a')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('id введен не корректно! Повторите ввод, используя функцию ввода')
    file_operation.write_file(array, 'a')
