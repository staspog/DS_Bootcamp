import sys

def names_extractor():
    if len(sys.argv) != 2:
        return
    
    # Получаем путь к файлу из аргумента
    file_path = sys.argv[1]
    
    # Открываем файл и читаем строки
    with open(file_path, 'r') as file:
        emails = file.read().strip().split('\n')
    
    # Создаем файл для результата
    with open('employees.tsv', 'w') as output_file:
        # Записываем заголовок
        output_file.write("Name\tSurname\tE-mail\n")
        
        # Обрабатываем каждый email
        for email in emails:
            # Получаем имя пользователя до @
            name_part = email.split('@')[0]
            
            # Разделяем имя и фамилию
            first_name, last_name = name_part.split('.')
            
            # Приводим к нужному формату (первая буква заглавная)
            first_name = first_name.capitalize()
            last_name = last_name.capitalize()
            
            # Записываем в файл
            output_file.write(f"{first_name}\t{last_name}\t{email}\n")

if __name__ == '__main__':
    names_extractor()