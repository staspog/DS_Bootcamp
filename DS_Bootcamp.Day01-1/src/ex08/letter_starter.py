import sys

def letter_starter():
    if len(sys.argv) != 2:
        return
    
    # Получаем email из аргумента
    target_email = sys.argv[1]
    
    # Читаем файл с данными
    with open('employees.tsv', 'r') as file:
        # Пропускаем заголовок
        next(file)
        
        # Ищем нужный email
        for line in file:
            # Разбиваем строку на колонки
            columns = line.strip().split('\t')
            
            # Проверяем, что строка имеет нужное количество колонок
            if len(columns) >= 3:
                name, surname, email = columns[0], columns[1], columns[2]
                
                # Нашли нужный email
                if email == target_email:
                    # Выводим приветственное письмо
                    print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That's a precondition for the professionals that our company hires.")
                    break

if __name__ == '__main__':
    letter_starter()