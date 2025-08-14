#!/bin/sh

# Создаем новый файл hh_uniq_positions.csv с заголовком
echo '"name","count"' > hh_uniq_positions.csv

tail -n +2 ../ex03/hh_positions.csv | awk -F, '{print $3}' | tr -d '"' \
| sort | uniq -c | sort -nr \
| awk '{print "\"" $2 "\"," $1}' >> hh_uniq_positions.csv