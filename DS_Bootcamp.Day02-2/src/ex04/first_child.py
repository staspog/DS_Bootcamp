import os
import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File '{self.path}' not found")
        
        with open(self.path, 'r') as file:
            lines = file.readlines()

        if len(lines) < (2 if has_header else 1):
            raise ValueError("Файл содержит недостаточно строк")
        
        if has_header:
            header = lines[0].strip().split(',')
            if len(header) != 2 or header != ['head', 'tail']:
                raise ValueError('Названия колонок не верны')

        data = []
        start_line = 1 if has_header else 0
        
        for line in lines[start_line:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['0', '1'], ['1', '0']]:
                raise ValueError('Некорректные данные в файле')
            data.append([int(values[0]), int(values[1])])
            
        return data

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails
        
        def fractions(self):
            heads, tails = self.counts()
            total = heads + tails
            return (heads / total * 100, tails / total * 100)

    class Analytics(Calculations):  # Наследуемся от Calculations
        def predict_random(self, n):
            return [[1, 0] if randint(0, 1) == 1 else [0, 1] for _ in range(n)]
        
        def predict_last(self):
            return self.data[-1]

def main():
    if len(sys.argv) != 2:
        raise ValueError('Указано неверное количество аргументов')
    
    try:
        research = Research(sys.argv[1])
        data = research.file_reader()
        
        analytics = research.Analytics(data)
        
        heads, tails = analytics.counts()
        head_pct, tail_pct = analytics.fractions()
        random_predictions = analytics.predict_random(3)
        last_prediction = analytics.predict_last()
        
        print(data)
        print(heads, tails)
        print(head_pct, tail_pct)
        print(random_predictions)
        print(last_prediction)
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()