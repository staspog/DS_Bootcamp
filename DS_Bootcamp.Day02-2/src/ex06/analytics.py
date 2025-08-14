import os
import logging
import json
from config import TELEGRAM_WEBHOOK_URL, TELEGRAM_CHAT_ID, report_template, num_of_steps
from random import randint
import requests

class Research:
    def __init__(self, path):
        self.path = path
        logging.info(f"Initialized Research with file: {self.path}")

    def file_reader(self, has_header=True):
        logging.info("Reading file")
        try:
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
            
            logging.info("File read successfully")
            return data

        except Exception as e:
            logging.error(f"Error reading file: {str(e)}")
            raise

    def send_telegram(self, success: bool):
        message = ("Я хоть и робот, но зато не мельник ебаный, как пиво бл" 
                   if success 
                   else "The report hasn’t been created due to an error")
        try:
            response = requests.post(
                TELEGRAM_WEBHOOK_URL,
                json={
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message
                }
            )
            logging.info(f"Telegram message sent: {message}")
        except Exception as e:
            logging.error(f"Failed to send Telegram message: {str(e)}")

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info("Initialized Calculations")

        def counts(self):
            logging.info("Calculating counts")
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            logging.info(f"Counts: heads={heads}, tails={tails}")
            return heads, tails
        
        def fractions(self):
            logging.info("Calculating fractions")
            heads, tails = self.counts()
            total = heads + tails
            result = (
                (heads / total * 100, tails / total * 100) 
                if total else (0.0, 0.0)
            )
            logging.info(f"Fractions: heads={result[0]:.2f}%, tails={result[1]:.2f}%")
            return result

    class Analytics(Calculations):
        def predict_random(self, n):
            logging.info(f"Generating {n} random predictions")
            predictions = [[1, 0] if randint(0, 1) else [0, 1] for _ in range(n)]
            logging.info(f"Predictions: {predictions}")
            return predictions
        
        def predict_last(self):
            logging.info("Getting last prediction")
            last = self.data[-1] if self.data else []
            logging.info(f"Last prediction: {last}")
            return last
        
        def save_file(self, data, filename, extension):
            logging.info(f"Saving file {filename}.{extension}")
            try:
                with open(f"{filename}.{extension}", 'w') as f:
                    f.write(data)
                logging.info("File saved successfully")
            except Exception as e:
                logging.error(f"Error saving file: {str(e)}")
                raise