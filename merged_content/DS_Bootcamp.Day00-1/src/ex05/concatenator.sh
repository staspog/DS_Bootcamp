#!/bin/sh

# Создаем итоговый файл и добавляем заголовок
echo '"id","created_at","name","has_test","alternate_url"' > hh_concatenated.csv

# Объединяем все файлы
cat *.csv | grep -v '"id","created_at","name","has_test","alternate_url"' >> hh_concatenated.csv