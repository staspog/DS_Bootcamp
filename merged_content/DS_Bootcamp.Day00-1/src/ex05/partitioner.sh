#!/bin/sh

tail -n +2 ../ex03/hh_positions.csv | sed 's/^\xEF\xBB\xBF//' | while IFS= read -r line; do
    # Извлекаем дату из created_at, удаляем кавычки
    date=$(echo "$line" | awk -F, '{gsub(/"/, "", $2); print $2}' | cut -d'T' -f1)
    
    # Создаем файл с заголовком, если он не существует
    if [ ! -f "$date.csv" ]; then
        echo '"id","created_at","name","has_test","alternate_url"' > "$date.csv"
    fi
    
    # Добавляем строку в файл
    echo "$line" >> "$date.csv"
done