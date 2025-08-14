import os
import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File '{self.path}' not found")
        
        with open (self.path) as file:
            lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("Файл должен содержать минимум две строки")
        
        header = lines[0].strip().split(',')
        if len(header) != 2 or header != ['head', 'tail']:
            raise ValueError('Названия колонок не верны')

        for line in lines[1:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['1', '0'], ['0', '1']]:
                raise ValueError('Некорректные данные в файле')
            
        return ''.join(lines)
        
def main():

    if len(sys.argv) != 2:
        raise ValueError('Указано неверное количество аргументов при запуске')
    
    try:
        research = Research(sys.argv[1])
        print(research.file_reader(), end='')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()