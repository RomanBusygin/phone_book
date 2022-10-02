def write_data(data):
    with open(path_file, 'a', encoding = 'utf8') as file:
        file.write(f'{data}\n')

def read_all_data():
    with open(path_file, 'r', encoding = 'utf8') as file:
        return file.readlines()

def delete_rec(data):
    with open(path_file, 'a', encoding = 'utf8') as file:
        file.write(f'{data}')

def clear_phone_book():
    with open(path_file, 'w', encoding = 'utf8') as file:
        file.write('')


path_file = r'C:\Users\Roman\Desktop\GEEK\Block_2\Phyton\Seminar\Sem_10\phone_book.txt'