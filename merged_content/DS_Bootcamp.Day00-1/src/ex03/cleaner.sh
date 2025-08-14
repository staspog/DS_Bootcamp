#!/bin/bash

# Создаем новый файл hh_positions.csv с заголовком
echo '"id","created_at","name","has_test","alternate_url"' > hh_positions.csv

# Обрабатываем каждую строку, начиная со второй
tail -n +2 ../ex02/hh_sorted.csv | while IFS= read -r line; do
    # Извлекаем название позиции
    position=$(echo "$line" | awk -F, '{print $3}' | tr -d '"')

    # Ищем слова "Junior", "Middle", "Senior"
    level=$(echo "$position" | grep -oE "Junior|Middle|Senior" | tr '\n' '/' | sed 's/\/$//')

    # Если ни одно из слов не найдено, заменяем на "-"
    if [ -z "$level" ]; then
        level="-"
    fi

    # Формируем новую строку
    new_line=$(echo "$line" | awk -v level="$level" -F, 'BEGIN {OFS=","} {$3="\"" level "\""; print}')

    # Добавляем строку в новый файл
    echo "$new_line" >> hh_positions.csv
done