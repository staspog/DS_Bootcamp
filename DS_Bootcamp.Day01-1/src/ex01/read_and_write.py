def parse_csv_line(line):
    columns = []
    current_column = []
    in_quotes = False

    i = 0
    while i < len(line):
        if line[i] == '"':
            in_quotes = not in_quotes
            current_column.append(line[i])
            i += 1
        elif line[i] == ',' and not in_quotes:
            columns.append(''.join(current_column))
            current_column = []
            i += 1
        else:
            current_column.append(line[i])
            i += 1

    columns.append(''.join(current_column))
    return columns

def read_and_write():
    """
    Читает CSV-файл, заменяет разделители на табуляцию и записывает в TSV-файл.
    """
    with open('ds.csv', 'r', encoding='utf-8') as csv_file, \
         open('ds.tsv', 'w', encoding='utf-8') as tsv_file:
        
        # Читаем файл построчно
        for line in csv_file:
            # Убираем символ новой строки
            line = line.rstrip('\n')
            # Разбираем строку на столбцы
            columns = parse_csv_line(line)
            # Объединяем столбцы через табуляцию
            tsv_line = '\t'.join(columns)
            # Записываем строку в TSV-файл
            tsv_file.write(tsv_line + '\n')

if __name__ == '__main__':
    read_and_write()