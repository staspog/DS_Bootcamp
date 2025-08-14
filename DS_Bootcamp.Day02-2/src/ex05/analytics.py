import os
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
            raise ValueError("File has insufficient lines")
        
        if has_header:
            header = lines[0].strip().split(',')
            if len(header) != 2 or header != ['head', 'tail']:
                raise ValueError('Invalid header')

        data = []
        start_line = 1 if has_header else 0
        
        for line in lines[start_line:]:
            values = line.strip().split(',')
            if len(values) != 2 or values not in [['0', '1'], ['1', '0']]:
                raise ValueError('Invalid data')
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
            return (heads / total * 100, tails / total * 100) if total else (0.0, 0.0)

    class Analytics(Calculations):
        def predict_random(self, n):
            return [[1, 0] if randint(0, 1) else [0, 1] for _ in range(n)]
        
        def predict_last(self):
            return self.data[-1] if self.data else []
        
        def save_file(self, data, filename, extension):
            with open(f"{filename}.{extension}", 'w') as f:
                f.write(data)