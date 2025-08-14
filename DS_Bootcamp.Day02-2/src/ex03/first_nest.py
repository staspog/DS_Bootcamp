import os
import sys

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header = True):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File '{self.path}' not found")
        
        with open (self.path) as file:
            lines = file.readlines()

        if len(lines) < (2 if has_header else 1):
            raise ValueError("Файл содержит недостаточно строк")
        
        if has_header == 1:
            header = lines[0].strip().split(',')
            if len(header) != 2 or header != ['head', 'tail']:
                raise ValueError('Названия колонок не верны')

        data = []
        for line in lines[1:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['1', '0'], ['0', '1']]:
                raise ValueError('Некорректные данные в файле')
            data.append([int(values[0]), int(values[1])])
            
        return data
    
    class Calculations:
        def counts(self, data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails
        
        def fractions(self, heads, tails):
            total = heads + tails
            return (heads / total * 100, tails / total * 100)

def main():

    if len(sys.argv) != 2:
        raise ValueError('Указано неверное количество аргументов при запуске')
    
    try:
        research = Research(sys.argv[1])
        data = research.file_reader()
        calc = research.Calculations()
        heads, tails = calc.counts(data)
        head_pct, tails_pct = calc.fractions(heads, tails)
        print(data)
        print(heads, tails)
        print(head_pct, tails_pct)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()